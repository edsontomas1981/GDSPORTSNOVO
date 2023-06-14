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
                return 310
            # Caso o produto não esteja cadastrado, realizar o cadastro
            lista = Lista_model(usuario_fk=user, produtos_fk_id=produto.obj_produto.id)
            lista.save()
            return 200
        except ObjectDoesNotExist:
            return 404
        except ValidationError:
            return 300
            
    def del_produto_lista_desejos(self, user, produto):
        try:
            # Verificar se o produto está cadastrado na lista de desejos do usuário
            lista = Lista_model.objects.filter(usuario_fk=user, produtos_fk__id=produto.obj_produto.id)
            if lista.exists():
                # Remover o produto da lista de desejos
                lista.delete()
                return 200
            else:
                return 310  # O produto não está na lista de desejos
        except ObjectDoesNotExist:
            return 404  # O usuário ou o produto não existem
        except ValidationError:
            return 300  # Erro de validação


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
