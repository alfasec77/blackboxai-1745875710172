from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess

class ScriptRequest(BaseModel):
    nome_script: str

router = APIRouter()

@router.post("/executar")
async def executar_script(request: ScriptRequest):
    try:
        # Exemplo: executar script OpenManus via subprocess
        processo = subprocess.run(
            ["python3", f"./scripts/{request.nome_script}.py"],
            capture_output=True,
            text=True,
            check=True
        )
        return {"saida": processo.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
