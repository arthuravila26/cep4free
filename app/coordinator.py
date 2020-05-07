from app.db.load import Load
from app.db.mongo_repository import Mongo
from app.configs.mongo_configs import MongoConfigs
from app.utils.logger import logger


class Coordinator:
    def __init__(self):
        self.mgdb = Mongo()
        load = Load()
        load.create_objects()
        self.can_execute = 0

    def run(self):
        logger.info("Busca de Cep inicializada...")
