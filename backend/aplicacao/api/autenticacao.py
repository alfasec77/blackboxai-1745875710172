from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from backend.aplicacao.seguranca.autenticacao import autenticar_usuario, criar_token_acesso
from fastapi.responses import JSONResponse
from datetime import timedelta

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = autenticar_usuario({"usuario1": {"username": "usuario1", "hashed_password": "$2b$12$KIXQ1Y6v1q6v1q6v1q6v1u", "disabled": False}}, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=60)
    access_token = criar_token_acesso(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return JSONResponse({"access_token": access_token, "token_type": "bearer"})
