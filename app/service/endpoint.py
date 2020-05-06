import http

from fastapi import FastAPI

from app.models.cep_validate import CepModel
from app.utils.logger import logger
from app.docs import *

app = FastAPI()

@app.get('/{Cep}')
def get_cep():
    cep = CepModel()
