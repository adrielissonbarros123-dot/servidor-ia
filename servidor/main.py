from fastapi import FastAPI

app = FastAPI(title="Servidor de IA")


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
