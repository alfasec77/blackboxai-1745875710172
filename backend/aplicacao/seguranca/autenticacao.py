from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional

# Configurações de segurança
SECRET_KEY = "sua_chave_secreta_muito_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Usuários simulados (substituir por banco de dados real)
fake_users_db = {
    "usuario1": {
        "username": "usuario1",
        "full_name": "Usuário Exemplo",
        "email": "usuario1@exemplo.com",
        "hashed_password": pwd_context.hash("senha123"),
        "disabled": False,
    }
}

def verificar_senha(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def obter_usuario(db, username: str):
    if username in db:
        user_dict = db[username]
        return user_dict
    return None

def autenticar_usuario(db, username: str, password: str):
    user = obter_usuario(db, username)
    if not user:
        return False
    if not verificar_senha(password, user["hashed_password"]):
        return False
    return user

def criar_token_acesso(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def obter_usuario_atual(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = obter_usuario(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user
