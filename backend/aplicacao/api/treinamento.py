from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess

class TreinamentoRequest(BaseModel):
    modelo: str
    caminho_dados: str

router = APIRouter()

@router.post("/iniciar")
async def iniciar_treinamento(request: TreinamentoRequest):
    try:
        # Exemplo: comando para iniciar treinamento com docling ou openmanus
        comando = f"python3 -m docling.treinar --modelo {request.modelo} --dados {request.caminho_dados}"
        processo = subprocess.run(
            comando,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return {"saida": processo.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
