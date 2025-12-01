from fastapi import FastAPI, HTTPException, Depends
from typing import List
from http import HTTPStatus
from models import User
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_session
from sqlalchemy.exc import IntegrityError
from importmaligno import (
    CreateReceita,
    Receita,
    Usuario,
    BaseUsuario,
    UsuarioPublic,
    validar_senha,
)

app = FastAPI(title="Api do Felps")


receitas: List[Receita] = []


@app.get("/")
def hello():
    return {"title": "Livro de Receitas"}


@app.get("/receitas", response_model=List[Receita], status_code=HTTPStatus.OK)
def get_todas_receitas():
    if len(receitas) == 0:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Sobrou Nada Pro Betinha"
        )
    return receitas


@app.get("/receitas/{receita}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita(receita: str):
    for i in receitas:
        if i.nome == receita:
            return i
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada"
    )


@app.post("/receitas", response_model=Receita, status_code=HTTPStatus.CREATED)
def criar_receita(dados: CreateReceita):
    id = len(receitas) + 1
    nova_receita = Receita(
        id=id,
        nome=dados.nome,
        ingredientes=dados.ingredientes,
        modo_de_preparo=dados.modo_de_preparo,
    )
    for i in receitas:
        if i.nome.upper() == nova_receita.nome.upper():
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT, detail="Receita já criada"
            )
    if 2 < len(nova_receita.nome) < 50:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Fora do Limite")
    receitas.append(nova_receita)
    return nova_receita


@app.get("/receitas/id/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_id(id: int):
    for i in receitas:
        if i.id == id:
            return i
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada"
    )


@app.put("/receitas/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def uptade_receita(id: int, dados: CreateReceita):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo,
            )
            for j in range(len(receitas)):
                if receitas[j].nome.upper() == receita_atualizada.nome.upper():
                    raise HTTPException(
                        status_code=HTTPStatus.CONFLICT,
                        detail="Já existe uma receita com esse nome",
                    )
            if receita_atualizada.nome == "":
                raise HTTPException(
                    status_code=HTTPStatus.BAD_REQUEST, detail="insira um nome"
                )
            receitas[i] = receita_atualizada
            return receita_atualizada
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada"
    )


@app.delete("/receitas/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def deletar_receia(id: int):
    if len(receitas) == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Não há Receitas")
    for i in range(len(receitas)):
        if receitas[i].id == id:
            m = receitas[i]
            receitas.pop(i)
            return m
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada"
    )


@app.post("/usuarios", status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_usuario(dados: BaseUsuario, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(
            (User.nome_usuario == dados.nome_usuario) | (User.email == dados.email)
        )
    )
    if db_user:
        if db_user.nome_usuario.upper() == dados.nome_usuario.upper():
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="já existe um beta com esse nome",
            )
        elif db_user.email.upper() == dados.email.upper():
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Já existe um Betinha com esse Email",
            )
        elif validar_senha(dados.senha) == False:
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="a senha deve ter numeros e caracteres",
            )
    db_user = User(
        nome_usuario=dados.nome_usuario, senha=dados.senha, email=dados.email
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get("/usuarios", status_code=HTTPStatus.OK, response_model=List[UsuarioPublic])
def get_todos_usuarios(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()

    return users


@app.get("/usuarios/{nome_usuarios}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuarios_por_nome(nome_usuario: str, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where((User.nome_usuario == nome_usuario)))
    if db_user:
        return db_user
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail="Betinha não encontrado"
    )


@app.get("/usuarios/id/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_id(id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == id))
    if db_user:
        return db_user
    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND, detail="Betinha não encontrado"
    )


@app.put("/usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def uptade_usuario(
    id: int, dados: BaseUsuario, session: Session = Depends(get_session)
):

    db_user = session.scalar(select(User).where(User.id == id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Betinha não encontrado"
        )
    try:
        db_user.nome_usuario = dados.nome_usuario
        db_user.senha = dados.senha
        db_user.email = dados.email
        session.commit()
        session.refresh(db_user)

        return db_user
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT, detail="Nome de usuario ou Email já existe"
        )


@app.delete("/usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def deletar_usuario(id: int, session: Session = Depends(get_session)):
    db_user = session.scalar(select(User).where(User.id == id))

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="Betinha não encontrado"
        )

    session.delete(db_user)
    session.commit()

    return db_user
