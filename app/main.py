from fastapi import FastAPI
from app.routes import users, agendamentos
from app.database import create_db

app = FastAPI(title="TimeBlocker API")

create_db()

app.include_router(users.router, prefix="/users")
app.include_router(agendamentos.router, prefix="/agendamentos")