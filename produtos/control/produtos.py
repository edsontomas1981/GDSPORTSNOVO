from produtos.models.produtos import Produtos as Mdl_produtos
from django.core.exceptions import ObjectDoesNotExist,ValidationError
import math


class Produtos:
    def __init__(self):
        self.obj_produto=Mdl_produtos()


    def save_or_update(self,dados):
            self.obj_produto.categoria_fk = dados['categoria_fk']
            self.obj_produto.subcategoria_fk = dados['subcategoria_fk']
            self.obj_produto.descricao = dados['descricao']
            self.obj_produto.marca = dados['marca']
            self.obj_produto.preco = dados['preco']
            self.obj_produto.cor = dados['cor']
            self.obj_produto.tamanho = dados['tamanho']
            self.obj_produto.obs = dados['obs']
            self.obj_produto.qtde = dados['qtde']
            self.obj_produto.save()


    def create_produto(self,dados):
        try:
            self.save_or_update(dados)
            return 200
        except:
            return 300


    def read_produto_id(self,id):
        try:
            if Mdl_produtos.objects.filter(id=id).exists:
                self.obj_produto=Mdl_produtos.objects.filter(id=id).get()
                return 200
            else:
                return 404
        except ObjectDoesNotExist:
            return 404
        except:
            return 300
        

    def read_produto_descricao(self,descricao):
        try:
            self.lista_produtos=[produto for produto in Mdl_produtos.objects.filter(descricao__icontains=descricao)]
            if len(self.lista_produtos)==0:
                return 404
            else:
                return 200
        except ObjectDoesNotExist:
            return 404
        except:
            return 300        


    def read_produto_categoria(self,categoria):
        try:
            self.lista_produtos=[produto for produto in Mdl_produtos.objects.filter(categoria_fk=categoria.obj_categoria.id)]
            if len(self.lista_produtos)==0:
                return 404
            else:
                return 200
        except ObjectDoesNotExist:
            return 404
        except:
            return 300    

    def read_produto_marca(self,marca):
        try:
            self.lista_produtos=[produto for produto in Mdl_produtos.objects.filter(marca__icontains=marca)]
            if len(self.lista_produtos)==0:
                return 404
            else:
                return 200
        except ObjectDoesNotExist:
            return 404
        except:
            return 300   
            
         
    def add_produto(self,qtde):
        try:
            if qtde<0:
                return 400 #numero negativo
            if str(qtde).isnumeric():
                self.obj_produto.qtde += qtde
                return 200
            else:
                return 401 #nao numerico            
        except:
            return 300
        

    def subtrai_produto(self,qtde):
        try:
            if str(qtde).isnumeric():
                if qtde>0:
                    self.obj_produto.qtde += qtde
                    return 200
                else:
                    return 400 #numero negativo
            else:
                return 401 #nao numerico
        except:
            return 300    
