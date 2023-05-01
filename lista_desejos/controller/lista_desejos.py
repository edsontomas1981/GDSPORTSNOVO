from lista_desejos.models.lista_desejos import Lista_desejos as Lista
from datetime import datetime


class Lista_desejos:
    def __init__(self):
        self.obj_lista_desejos=Lista()

    def create_or_update(self,dados):
        data_hora_atual = datetime.now()
        self.obj_lista_desejos.data=data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        self.obj_lista_desejos.produtos_fk=dados['produto']
        self.obj_lista_desejos.usuario_fk=dados['usuario']
        self.obj_lista_desejos.save()

    def create_lista_desejos(self,dados):
        # self.create_or_update(dados)
        return 200
       
