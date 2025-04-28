from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.7
    top_p: float = 0.9

router = APIRouter()

# Load model and tokenizer once
MODEL_NAME = "EleutherAI/gpt-neo-125M"
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to(device)

@router.post("/gerar")
async def gerar_texto(request: PromptRequest):
    try:
        inputs = tokenizer(request.prompt, return_tensors="pt").to(device)
        output = model.generate(
            **inputs,
            max_length=request.max_length + inputs.input_ids.shape[1],
            temperature=request.temperature,
            top_p=request.top_p,
            do_sample=True,
            num_return_sequences=1,
        )
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        # Remove prompt from generated text if present
        if generated_text.startswith(request.prompt):
            generated_text = generated_text[len(request.prompt):]
        return {"texto_gerado": generated_text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
