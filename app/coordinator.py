import uvicorn

from app.db.load import Load
from app.db.mongo_repository import Mongo
from app.utils.logger import logger
from app.service.endpoint import FastAPI, app


class Coordinator:
    def __init__(self):
        self.app = FastAPI()
        self.mgdb = Mongo()
        load = Load()
        load.create_objects()
        self.can_execute = 0

    def run(self):
        uvicorn.run(app)
        logger.info("Busca de Cep finalizada...")
