import requests
import mongoengine
import json

from fastapi import FastAPI
from app.db.CEP import CEP
from app.utils.logger import logger
from app.db.load import Load

app = FastAPI()


@app.get('/cep/{cep}')
def find_ceps(cep):
    ceps = CEP.objects.get(cep=cep).to_json()
    return json.loads(ceps)
