from pydantic import BaseModel, validator


class CepModel(BaseModel):
    cep = str
    cidade = str
    bairro = str
    endereco = str

    @validator('cep')
    def max_lenght_cep(cls, value):
        if len(value) > 8 or len(value) < 8:
            raise ValueError('O CEP precisa ter 8 números')
        return value
