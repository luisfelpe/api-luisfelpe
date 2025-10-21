from fastapi import FastAPI, HTTPException
from typing import List
from http import HTTPStatus
from .schema import CreateReceita,Receita

app = FastAPI(title="Api do Felps")


receitas: List[Receita] = []


@app.get("/")
def hello():
    return {"title": "Livro de Receitas"}


@app.get("/receitas", response_model=List[Receita], status_code=HTTPStatus.OK)
def get_todas_receitas():
    if len(receitas) == 0:
        raise HTTPException(status_code=HTTPException.NOT_FOUND, detail="Sobrou Nada Pro Betinha")
    return receitas


@app.get("/receitas/{receita}", response_model=List[Receita], status_code=HTTPStatus.OK)
def get_receita(receita: str):
    for i in receitas:
        if i.nome == receita:
            return i
    raise HTTPException(status_code=HTTPException.NOT_FOUND, detail="Receita não encontrada")


@app.post("/receitas", response_model=List[Receita], status_code=HTTPStatus.CREATED)
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
            raise HTTPException(status_code=HTTPException.BAD_REQUEST, detail="Receita já criada")
    if 2 > len(nova_receita.nome) > 50:
        raise HTTPException(status_code=HTTPException.BAD_REQUEST, detail="Fora do Limite")
    receitas.append(nova_receita)
    return nova_receita


@app.get("/receitas/id/{id}", response_model=List[Receita], status_code=HTTPStatus.OK)
def get_receita_por_id(id: int):
    for i in receitas:
        if i.id == id:
            return i
    raise HTTPException(status_code=HTTPException.NOT_FOUND, detail="Receita não encontrada")


@app.put("/receitas/{id}", response_model=List[Receita], status_code=HTTPStatus.OK)
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
                    raise HTTPException(status_code=HTTPException.CONFLICT, detail="Já existe uma receita com esse nome")
            if receita_atualizada.nome == "":
                raise HTTPException(status_code=HTTPException.BAD_REQUEST, detail="insira um nome")
            receitas[i] = receita_atualizada
            return receita_atualizada
    raise HTTPException(status_code=HTTPException.NOT_FOUND, detail="Receita não encontrada")


@app.delete("/receitas/{id}", response_model=List[Receita], status_code=HTTPStatus.OK)
def deletar_receia(id: int):
    if len(receitas) == 0:
        raise HTTPException(status_code=HTTPException.NOT_FOUND, detail="Não há Receitas")
    for i in range(len(receitas)):
        if receitas[i].id == id:
            m = receitas[i].nome
            receitas.pop(i)
            return {"mensagem": "A Receita " + m + " Foi Deletada:"}
    raise HTTPException(status_code=HTTPException.NOT_FOUND, detail="Receita não encontrada")
