from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI(title="Api do Felps")

class Receita(BaseModel):
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
    for receita in receitas:
        if receita.nome==receita:
            return receita.ingredientes
    return{"Receita não encontrada"}
        
        
@app.post("/receitas", response_model=Receita, status_code=201)
def criar_receita(dados: Receita):
    nova_receita=dados
    for i in receitas:
        if receitas.nome.upper()==nova_receita.nome.upper():
            return("Receita já criada")
        else:
            receitas.append(nova_receita)
            return nova_receita


    