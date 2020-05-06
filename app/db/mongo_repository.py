import mongoengine
from app.utils.logger import logger
from app.configs.mongo_configs import MongoConfigs

class Mongo:
    def __init__(self):
        self.settings = MongoConfigs
        self.__connect()

    def __connect(self):
        logger.info('Conneting to DB')
        mongoengine.connect(host=MongoConfigs.MONGO_URI)
        logger.info('Connected to DB')