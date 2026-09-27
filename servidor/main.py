from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(title="Servidor de IA")
class Tarefa(BaseModel):
    tarefa: str

@app.get("/")
def inicio():
    return {
        "status": "online",
        "mensagem": "Servidor de IA funcionando!",
        "agentes": {
            "gemini": "coordenador",
            "openai": "programacao_e_raciocinio",
            "claude": "analise_e_revisao",
            "mistral": "codigo_e_agentes",
            "local": "modelos_locais"
        }
    }
@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/tarefa")
def criar_tarefa(tarefa: Tarefa):
    return {
        "status": "recebida",
        "tarefa": tarefa.tarefa
    }
