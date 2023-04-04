from produtos.models.tamanhos import Tamanhos as Mdl_tamanhos

class Tamanhos:
    def __init__(self) -> None:
        self.obj_tamanho = Mdl_tamanhos()
    

    def save_or_update(self,dados):
        self.obj_tamanho.tamanho=dados['tamanho']
        self.obj_tamanho.save()


    def create_tamanho(self,dados):
        try:
            self.save_or_update(dados)
            return 200
        except:
            return 300


    def read_tamanho(self,id):
        try:
            if Mdl_tamanhos.objects.filter(id=id).exists():
                self.obj_tamanho=Mdl_tamanhos.objects.filter(id=id).get()
                return 200
            else:
                return 404
        except:
            return 300


    def update_tamanho(self,id,dados):
        try:
            if Mdl_tamanhos.objects.filter(id=id).exists():
                self.obj_tamanho=Mdl_tamanhos.objects.filter(id=id).get()
                self.save_or_update(dados)
                return 200
            else:
                return 404
        except:
            return 300

    def delete_tamanho(self,id):
        try:
            if Mdl_tamanhos.objects.filter(id=id).exists():
                self.obj_tamanho=Mdl_tamanhos.objects.filter(id=id).get()
                self.obj_tamanho.delete()
                return 200
            else:
                return 404
        except:
            return 300
