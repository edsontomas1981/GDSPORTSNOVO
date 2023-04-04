from produtos.models.cores import Cores as Mdl_cores

class Cores:
    def __init__(self) -> None:
        self.obj_cor = Mdl_cores()
    

    def save_or_update(self,dados):
        self.obj_cor.cor=dados['cor']
        self.obj_cor.save()


    def create_cor(self,dados):
        try:
            self.save_or_update(dados)
            return 200
        except:
            return 300


    def read_cor(self,id):
        try:
            if Mdl_cores.objects.filter(id=id).exists():
                self.obj_cor=Mdl_cores.objects.filter(id=id).get()
                return 200
            else:
                return 404
        except:
            return 300


    def update_cor(self,id,dados):
        try:
            if Mdl_cores.objects.filter(id=id).exists():
                self.obj_cor=Mdl_cores.objects.filter(id=id).get()
                self.save_or_update(dados)
                return 200
            else:
                return 404
        except:
            return 300

    def delete_cor(self,id):
        try:
            if Mdl_cores.objects.filter(id=id).exists():
                self.obj_cor=Mdl_cores.objects.filter(id=id).get()
                self.obj_cor.delete()
                return 200
            else:
                return 404
        except:
            return 300