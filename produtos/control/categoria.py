from produtos.models.categoria import Categoria as Mdl_categoria
class Categoria:
    def __init__(self):
        self.obj_categoria=Mdl_categoria()
    def save_or_update(self,dados):
        self.obj_categoria.categoria=dados['categoria']
        self.obj_categoria.save()
        

    def create_categoria(self,dados):
        try:
            self.save_or_update(dados)
            return 200
        except:
            return 300


    def read_categoria(self,id):
        try:
            if Mdl_categoria.objects.filter(id=id).exists():
                self.obj_categoria=Mdl_categoria.objects.filter(id=id).get()
                return 200
            else:
                return 404
        except:
            return 300


    def update_categoria(self,id,dados):
        try:
            if Mdl_categoria.objects.filter(id=id).exists():
                self.obj_categoria=Mdl_categoria.objects.filter(id=id).get()
                self.save_or_update(dados)
                return 200
            else:
                return 404
        except:
            return 300
        
        
    def delete_categoria(self,id):
        try:
            if Mdl_categoria.objects.filter(id=id).exists():
                self.obj_categoria=Mdl_categoria.objects.filter(id=id).get()
                self.obj_categoria.delete()
                return 200
            else:
                return 404
        except:
            return 300