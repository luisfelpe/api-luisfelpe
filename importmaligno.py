from pydantic import BaseModel
from typing import List

class CreateReceita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str


class Receita(BaseModel):
    id: int
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

class Usuario(BaseModel):
    id: int
    nome_usuario: str
    email: str
    senha: str

class BaseUsuario(BaseModel):
    nome_usuario: str
    email: str
    senha: str

class UsuarioPublic(BaseModel):
    id: int
    nome_usuario: str
    email: str
def validar_senha(x):
    count_n=0
    count_l=0
    for i in x:
        if i.isdigit():
            count_n+=1
        elif i.isalpha():
            count_l+=1
    if count_n==0 or count_l==0:
        return False
    return True