from django.test import TestCase
from produtos.control.categoria import Categoria
from produtos.control.subcategoria import Subcategoria

class Carrinho_test(TestCase):
    def setUp(self):
        self.categoria=Categoria()
        self.subcategoria=Subcategoria()

    def test_carrinho(self):
        dados = {'categoria':"Brasileirão"}
        dados_erro = {}
