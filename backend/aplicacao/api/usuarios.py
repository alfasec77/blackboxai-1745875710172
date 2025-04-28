from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr
from backend.aplicacao.seguranca.autenticacao import pwd_context, fake_users_db, obter_usuario, criar_token_acesso
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

router = APIRouter()

class UsuarioCadastro(BaseModel):
    username: str
    email: EmailStr
    password: str

@router.post("/registrar", status_code=status.HTTP_201_CREATED)
async def registrar_usuario(usuario: UsuarioCadastro):
    if usuario.username in fake_users_db:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    hashed_password = pwd_context.hash(usuario.password)
    fake_users_db[usuario.username] = {
        "username": usuario.username,
        "email": usuario.email,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    return {"msg": "Usuário registrado com sucesso"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = obter_usuario(fake_users_db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    access_token_expires = timedelta(minutes=60)
    access_token = criar_token_acesso(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
