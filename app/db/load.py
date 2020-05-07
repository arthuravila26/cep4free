import json
import os
import csv
import mongoengine

from app.db.CEP import CEP
from app.utils.logger import logger


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
            filename = os.path.join(dir_path, 'ceps.txt')
            with open(filename, newline='') as ceps:
                ceps_reader = csv.reader(ceps, delimiter='\t')
                for cep in ceps_reader:
                    c = CEP()
                    c.cep = cep[0]
                    c.cidade = cep[1]
                    c.bairro = cep[2]
                    c.endereco = cep[3]
                    c.save()
        else:
            logger.info('Os CEPs já foram inseridos na base de dados.')
