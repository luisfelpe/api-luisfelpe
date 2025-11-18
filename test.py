from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import User, tabela_registro

app = FastAPI(title='API de teste')

engine = create_engine("sqlite:///:memory:", echo=False)

tabela_registro.metadata.create_all(engine)

with Session(engine) as session:
    Felps = User(
        nome_usuario="Felipe", senha="4002-8922", email="darkwraith@opmail.com"
    )
    session.add(Felps)
    session.commit()
    session.refresh(Felps)

print("Dados do usuario:", Felps)
print("ID:", Felps.id)
print("Criado em:", Felps.created_at)
print("atualizado em:", Felps.updated_at)