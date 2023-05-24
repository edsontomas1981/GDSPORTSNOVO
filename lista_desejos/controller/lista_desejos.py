from lista_desejos.models.lista_desejos import Lista_desejos as ListaModel
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.models import User
from produtos.models.produtos import Produtos
from datetime import datetime

class Lista_desejos:
    def __init__(self):
        self.obj_lista_desejos = ListaModel()

    def create_or_update(self, dados):
        pass

    def create_lista_desejos(self, dados):
        user_id = dados['user'].id
        user = User.objects.get(id=user_id)
        produto_id = dados['produtoId']
        produto = Produtos.objects.get(id=produto_id)

        self.obj_lista_desejos.usuario_fk = user
        self.obj_lista_desejos.save()

        self.obj_lista_desejos.produtos_fk.add(produto)
        return 200

    def read_lista(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            lista_desejos = ListaModel.objects.get(usuario_fk=user)
            return 200
        except ObjectDoesNotExist:
            return 404
        except ValidationError:
            return 300
