from produtos.models.subcategoria import Subcategoria as Mdl_subcategoria

class Subcategoria:
    def __init__(self):
        self.obj_subcategoria = Mdl_subcategoria()

    def save_or_update(self, dados):
        self.obj_subcategoria.descricao = dados['descricao']
        self.obj_subcategoria.categoria_fk = dados['categoria']
        self.obj_subcategoria.save()

    def create_subcategoria(self, dados):
        try:
            self.save_or_update(dados)
            return 200
        except:
            return 300

    def read_subcategoria(self, id):
        try:
            if Mdl_subcategoria.objects.filter(id=id).exists():
                self.obj_categoria = Mdl_subcategoria.objects.filter(id=id).get()
                return 200
            else:
                return 404
        except:
            return 300

    def update_subcategoria(self, id, dados):
        try:
            if Mdl_subcategoria.objects.filter(id=id).exists():
                self.obj_subcategoria = Mdl_subcategoria.objects.filter(id=id).get()
                self.save_or_update(dados)
                return 200
            else:
                return 404
        except:
            return 300

    def delete_subcategoria(self, id):
        try:
            if Mdl_subcategoria.objects.filter(id=id).exists():
                self.obj_subcategoria = Mdl_subcategoria.objects.filter(id=id).get()
                self.obj_subcategoria.delete()
                return 200
            else:
                return 404
        except:
            return 300
