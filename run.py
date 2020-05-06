from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"cep": "01001000",	"cidade": "São Paulo", "uf": "SP", "bairro": "Sé", "endereço": "Praça da Sé - lado ímpar"}
