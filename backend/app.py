from fastapi import FastAPI
from backend.aplicacao.api import (
    gpt_neo_router,
    openmanus_router,
    treinamento_router,
    docling_treinamento_router,
    autenticacao_router,
    usuarios_router,
)

app = FastAPI(title="Agente Mano DEV API")

app.include_router(gpt_neo_router, prefix="/api/gpt-neo")
app.include_router(openmanus_router, prefix="/api/openmanus")
app.include_router(treinamento_router, prefix="/api/treinamento")
app.include_router(docling_treinamento_router, prefix="/api/docling")
app.include_router(autenticacao_router, prefix="/api/auth")
app.include_router(usuarios_router, prefix="/api/usuarios")

@app.get("/")
async def root():
    return {"mensagem": "API do Agente Mano DEV está online"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
