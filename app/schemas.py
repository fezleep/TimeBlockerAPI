from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class AgendamentoBase(BaseModel):
    titulo: str
    data_hora: datetime
    descricao: Optional[str] = None

class AgendamentoCreate(AgendamentoBase):
    pass

class AgendamentoOut(AgendamentoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True