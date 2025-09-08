from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI(title="Api do Felps")

class CreateReceita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str
class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str      

receitas: List[Receita]=[]

@app.get("/")
def hello():
    return{"title": "Livro de Receitas"}
@app.get("/receitas")
def get_todas_receitas():
    return receitas
@app.get("/receitas/{receita}")
def get_receita(receita: str):
    for i in receitas:
        if i.nome==receita:
            return i
    return{"mensagem: Receita não encontrada"}
                
@app.post("/receitas")
def criar_receita(dados: CreateReceita):
    id=len(receitas)+1
    nova_receita=Receita(id=id,nome=dados.nome,ingredientes=dados.ingredientes,modo_de_preparo=dados.modo_de_preparo)
    for i in receitas:
        if i.nome.upper()==nova_receita.nome.upper():
            return("mensagem: Receita já criada")
    if 2>len(nova_receita.nome)>50:
        return{"mensagem: Fora do Limite"}      
    receitas.append(nova_receita)
    return nova_receita        
@app.get("/receitas/id/{id}")
def get_receita_por_id(id: int):
    for i in receitas:
        if i.id==id:
            return i
    return{"mensagem: Receita não encontrada"}

@app.put("/receitas{id}")
def uptade_receita(id: int, dados: CreateReceita):
    for i in range(len(receitas)):
        if receitas[i].id==id:
            receita_atualizada=Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo,
            )
            for j in range(len(receitas)):
                if receitas[j].nome.upper()==receita_atualizada.nome.upper():
                    return{"mensagem: Já existe uma receita com esse nome"}
            if receita_atualizada.nome=="":
                return{"mensagem: insira um nome"}
            if 2>len(receita_atualizada.nome)>50:
                return{"mensagem: Fora do Limite"}
            receitas[i]=receita_atualizada
            return receita_atualizada
    return{"mensagem: Receita não encontrada"}