from django.test import TestCase
from produtos.control.categoria import Categoria
from produtos.control.subcategoria import Subcategoria
from produtos.control.produtos import Produtos
from produtos.control.cores import Cores
from produtos.control.tamanho import Tamanhos

class Categoria_test(TestCase):
    def setUp(self):
        self.categoria=Categoria()
        self.subcategoria=Subcategoria()
        self.produto = Produtos()
        self.cor = Cores()
        self.tamanho = Tamanhos()
        dados_categoria = {'categoria' : "Brasileirão"}
        dados_cores = {'cor' : 'Preta'}
        dados_tamanho = {'tamanho' : 'GG'}
        self.categoria.create_categoria(dados_categoria)
        self.cor.create_cor(dados_cores)
        self.tamanho.create_tamanho(dados_tamanho)
        dados_sub = {'descricao': "Corinthians", 'categoria': self.categoria.obj_categoria}
        self.subcategoria.create_subcategoria(dados_sub)      

    def test_produtos(self):
        # Gera dados
        dados_erro={}
        dados_produto={'categoria_fk' :self.categoria.obj_categoria,
                       'subcategoria_fk':self.subcategoria.obj_subcategoria,
                       'descricao':'Camisa 2023','marca':'Nike','preco':125.00,
                       'cor':self.cor.obj_cor,'tamanho':self.tamanho.obj_tamanho
                       ,'obs':'Observação','qtde':10}

    #Cria Produto
        self.assertEqual(self.produto.create_produto(dados_produto),200)
        self.assertEqual(self.produto.create_produto(dados_erro),300)

    #Buscas diversas
        #Busca por id
        self.assertEqual(self.produto.read_produto_id(1),200)
        self.assertEqual(self.produto.read_produto_id(2),404)
        
        #Busca por descrição
        self.assertEqual(self.produto.read_produto_descricao('Camisa'),200)
        self.assertEqual(len(self.produto.lista_produtos),1)
        self.assertEqual(self.produto.read_produto_descricao('Boné'),404)
        self.assertEqual(len(self.produto.lista_produtos),0)

        #Busca por categoria
        self.assertEqual(self.produto.read_produto_categoria(self.categoria),200)
        self.assertEqual(len(self.produto.lista_produtos),1)
        self.categoria1=Categoria()
        dados_categoria = {'categoria':"Europa"}
        self.categoria1.create_categoria(dados_categoria)
        self.assertEqual(self.produto.read_produto_categoria(self.categoria1),404)
        self.assertEqual(len(self.produto.lista_produtos),0)
        self.assertEqual(self.produto.read_produto_categoria(dados_erro),300)
        self.assertEqual(len(self.produto.lista_produtos),0)
        #Busca por marca
        self.assertEqual(self.produto.read_produto_marca('Nike'),200)
        self.assertEqual(len(self.produto.lista_produtos),1)
        self.assertEqual(self.produto.read_produto_marca('Adidas'),404)
        self.assertEqual(len(self.produto.lista_produtos),0)        

    #Atualizar produto        
        dados_erro={}
        dados_produto={'categoria_fk':self.categoria.obj_categoria,
                       'subcategoria_fk':self.subcategoria.obj_subcategoria,
                       'descricao':'Camisa 2024','marca':'Adidas','preco':130.00,
                       'cor':self.cor.obj_cor,'tamanho':self.tamanho.obj_tamanho
                       ,'obs':'Observação','qtde':45}
        self.assertEqual(self.produto.update_produto(1,dados_produto),200)
        self.assertEqual(self.produto.obj_produto.descricao,'Camisa 2024')
        self.assertEqual(self.produto.obj_produto.marca,'Adidas')
        self.assertEqual(self.produto.obj_produto.preco,130.00)
        self.assertEqual(self.produto.update_produto(1,dados_erro),300)
    
        self.assertEqual(self.produto.obj_produto.qtde,45)
        self.assertEqual(self.produto.add_produto(1),200)
        self.assertEqual(self.produto.obj_produto.qtde,46)
        self.assertEqual(self.produto.add_produto(-1),401)#deve ser um numero inteiro
        self.assertEqual(self.produto.add_produto('a'),401)#deve ser um numero inteiro
        self.assertEqual(self.produto.add_produto(1.06),401)#deve ser um numero inteiro

        self.assertEqual(self.produto.subtrai_produto(2),200)
        self.assertEqual(self.produto.obj_produto.qtde,44)
        self.assertEqual(self.produto.subtrai_produto('a'),401)#deve ser um numero inteiro
        self.assertEqual(self.produto.subtrai_produto(1.06),401) #deve ser um numero inteiro
        self.assertEqual(self.produto.obj_produto.qtde,44)
        self.assertEqual(self.produto.subtrai_produto(70),402)#Retirada maior do que estoque
        self.assertEqual(self.produto.obj_produto.qtde,44)

        self.assertEqual(self.produto.delete_produto(dados_erro), 300)
        self.assertEqual(self.produto.read_produto_id(1), 200)
        self.assertEqual(self.produto.delete_produto(1), 200)
        self.assertEqual(self.produto.read_produto_id(1), 404)







        




        
    
        



        