from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AgendamentoOut)
def criar_agendamento(agendamento: schemas.AgendamentoCreate, db: Session = Depends(get_db)):
    novo_agendamento = models.Agendamento(**agendamento.dict(), owner_id=1)  # ID fixo por enquanto
    db.add(novo_agendamento)
    db.commit()
    db.refresh(novo_agendamento)
    return novo_agendamento

@router.get("/", response_model=List[schemas.AgendamentoOut])
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(models.Agendamento).filter(models.Agendamento.owner_id == 1).all()  # ID fixo por enquanto
