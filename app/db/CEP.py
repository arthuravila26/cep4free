from mongoengine import Document, StringField, queryset_manager


class CEP(Document):
    cep = StringField(required=True)
    cidade = StringField(required=True)
    bairro = StringField(required=True)
    endereco = StringField(required=True)

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)

    @queryset_manager
    def get_by_cep(doc_cls, queryset, cep):
        cep = queryset(cep=cep).first()

    meta = {
        'cep': 'ceps',
    }
