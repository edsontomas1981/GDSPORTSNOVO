from lista_desejos.models.lista_desejos import Lista_desejos as Lista_model
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from datetime import datetime

class Lista_desejos:
    def __init__(self):
        self.obj_lista_desejos = Lista_model()

    def create_or_update(self, dados):
        pass

    def add_produto_lista_desejos(self,  user,produto):
        try:
            # Verificar se o produto já está cadastrado na lista de desejos do usuário
            lista = Lista_model.objects.filter(usuario_fk=user, produtos_fk__id=produto.obj_produto.id)
            if lista.exists():
                print(310)
                return 310

            # Caso o produto não esteja cadastrado, realizar o cadastro
            lista = Lista_model(usuario_fk=user, produtos_fk_id=produto.obj_produto.id)
            lista.save()
            return 200
        except ObjectDoesNotExist:
            return 404
        except ValidationError:
            return 300

    def read_lista(self, user):
        try:
            # Verificar se o produto já está cadastrado na lista de desejos do usuário
            lista = Lista_model.objects.filter(usuario_fk=user)
            if lista.exists():
                return Lista_model.objects.filter(usuario_fk=user)
        except ObjectDoesNotExist:
            return 404
        except ValidationError:
            return 300
