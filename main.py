from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from database import init_db, session_local
from models import Usuario as Usuario_model
from contextlib import asynccontextmanager
import uuid

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    print("Servidor desligando...")

app = FastAPI(lifespan=lifespan)

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

class Usuario(BaseModel):
    nome:str
    idade:int
    email:EmailStr

@app.post("/usuarios/",status_code=status.HTTP_201_CREATED)
def create_user(usuario: Usuario, db: Session = Depends(get_db)):
    id_unico = str(uuid.uuid4())
    db_usuario = Usuario_model(
        id = id_unico,
        nome = usuario.nome,
        idade = usuario.idade,
        email = usuario.email
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return {"mensagem":f"Usuario {usuario.nome} criado com sucesso id:{id_unico}"}

@app.get("/usuarios/",status_code=status.HTTP_200_OK)
def list_users(db : Session = Depends(get_db)):
    usuarios = db.query(Usuario_model).all()
    return {"usuarios":usuarios}

@app.put("/usuarios/{usuario_id}")
def update_user(usuario_id:str, usuario: Usuario, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario_model).filter_by(id=usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db_usuario.nome = usuario.nome
    db_usuario.idade = usuario.idade
    db_usuario.email = usuario.email
    db.commit()
    db.refresh(db_usuario)

    return {"mensagem": f"Usuário {usuario_id} atualizado com sucesso"}

@app.delete("/usuarios/{usuario_id}", status_code=status.HTTP_200_OK)
def delete_user(usuario_id:str, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario_model).filter_by(id=usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(db_usuario)
    db.commit()
    return {"mensagem": f"Usuário {usuario_id} excluído com sucesso!"}

