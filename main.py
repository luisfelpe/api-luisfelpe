from fastapi import FastAPI, HTTPException
from typing import List
from http import HTTPStatus
from importmaligno import CreateReceita, Receita, Usuario, BaseUsuario, UsuarioPublic

app = FastAPI(title="Api do Felps")


receitas: List[Receita] = []

usuarios: List[Usuario] = []

@app.get("/")
def hello():
    return {"title": "Livro de Receitas"}


@app.get("/receitas", response_model=List[Receita], status_code=HTTPStatus.OK)
def get_todas_receitas():
    if len(receitas) == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Sobrou Nada Pro Betinha")
    return receitas


@app.get("/receitas/{receita}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita(receita: str):
    for i in receitas:
        if i.nome == receita:
            return i
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")


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
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Receita já criada")
    if 2 > len(nova_receita.nome) > 50:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="Fora do Limite")
    receitas.append(nova_receita)
    return nova_receita


@app.get("/receitas/id/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_id(id: int):
    for i in receitas:
        if i.id == id:
            return i
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")


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
                    raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Já existe uma receita com esse nome")
            if receita_atualizada.nome == "":
                raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="insira um nome")
            receitas[i] = receita_atualizada
            return receita_atualizada
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")


@app.delete("/receitas/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def deletar_receia(id: int):
    if len(receitas) == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Não há Receitas")
    for i in range(len(receitas)):
        if receitas[i].id == id:
            m = receitas[i].nome
            receitas.pop(i)
            return m
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")

@app.post("/usuarios", status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_usuario(dados: BaseUsuario):
    id = len(usuarios) + 1
    novo_usuario = Usuario(
        id=id,
        nome_usuario=dados.nome_usuario,
        email=dados.email,
        senha=dados.senha,
    )
    for i in usuarios:
        if i.email.upper==novo_usuario.email.upper:
            raise HTTPException(status_code=HTTPStatus.CONFLICT, detail="Já existe um Usuario com esse Email")
    usuarios.append(novo_usuario)
    return novo_usuario
@app.get("/usuarios", status_code=HTTPStatus.OK, response_model=List[UsuarioPublic])
def get_todos_usuarios():
    if len(usuarios) == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Sobrou nenhum Betinha")
    return usuarios

@app.get("/usuarios/{nome_usuarios}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuarios_por_nome(nome_usuario: str):
    for i in usuarios:
        if i.nome_usuario == nome_usuario:
            return i
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="usuario não encontrado")

@app.get("/usuarios/id/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_id(id: int):
    for i in usuarios:
        if i.id == id:
            return i
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuario não encontrado")