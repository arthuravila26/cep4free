import json
import os

import mongoengine

from app.db.CEP import CEP
from  app.utils.logger import logger

class Load:

    @staticmethod
    def connect():
        mongoengine.connect(host=os.getenv('MONGO_URI'))

    def create_objects(self):
        self.create_ceps()

    def create_ceps(self):
        if CEP.objects.count() == 0:
            logger.info('Inserindo dados no DB')
            dir_path = os.path.dirname(os.path.realpath(__file__))
            filename = os.path.join(dir_path, 'CEP', 'cep.json')
            with open(filename) as json_file:
                data = json.load(json_file)
                for cep in data:
                    cep = CEP(cep=cep['Cep'],
                              cidade=cep['Cidade'],
                              uf=cep['UF'],
                              bairro=cep['Bairro'],
                              endereco=cep['Endereco'])
                    cep.save()
        else:
            logger.info('Os CEPs já foram inseridos na base de dados.')