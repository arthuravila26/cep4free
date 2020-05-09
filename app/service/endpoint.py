import json

from fastapi import FastAPI
from app.db.CEP import CEP


app = FastAPI()


@app.get('/cep/{cep}')
def find_ceps(cep):
    ceps = CEP.objects.get(cep=cep).to_json()
    return json.loads(ceps)
