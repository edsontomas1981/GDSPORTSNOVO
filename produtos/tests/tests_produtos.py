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
        self.produto=Produtos()
        self.cor= Cores()
        self.tamanho= Tamanhos()
        dados_categoria = {'categoria':"Brasileirão"}
        dados_cores={'cor':'Preta'}
        dados_tamanho={'tamanho':'GG'}
        self.categoria.create_categoria(dados_categoria)
        self.cor.create_cor(dados_cores)
        self.tamanho.create_tamanho(dados_tamanho)
        dados_sub = {'descricao': "Corinthians", 'categoria': self.categoria.obj_categoria}
        self.subcategoria.create_subcategoria(dados_sub)      

    def test_produtos(self):
        dados_erro={}
        dados_produto={'categoria_fk':self.categoria.obj_categoria,
                       'subcategoria_fk':self.subcategoria.obj_subcategoria,
                       'descricao':'Camisa 2023','marca':'Nike','preco':125.00,
                       'cor':self.cor.obj_cor,'tamanho':self.tamanho.obj_tamanho
                       ,'obs':'Observação'}

        self.assertEqual(self.produto.create_produto(dados_produto),200)
        self.assertEqual(self.produto.create_produto(dados_erro),300)

        self.assertEqual(self.produto.read_produto_id(1),200)
        self.assertEqual(self.produto.read_produto_id(2),404)




        
    
        



        