from django.test import TestCase
from produtos.control.categoria import Categoria
from produtos.control.subcategoria import Subcategoria

class Categoria_test(TestCase):
    def setUp(self):
        self.categoria=Categoria()
        self.subcategoria=Subcategoria()


    def test_categoria(self):
        dados = {'categoria':"Brasileirão"}
        dados_erro = {}
        '''teste de criação de categoria'''
        self.assertEqual(self.categoria.create_categoria(dados), 200)
        self.assertEqual(self.categoria.create_categoria(dados_erro), 300)

        '''teste de read Categoria'''
        self.assertEqual(self.categoria.read_categoria(1), 200)
        self.assertEqual(self.categoria.read_categoria(2), 404)

        dados = {'categoria': "Europa"}
        '''teste de update'''
        self.assertEqual(self.categoria.update_categoria(1, dados), 200)
        self.assertEqual(self.categoria.update_categoria(1, dados_erro), 300)
        self.assertEqual(self.categoria.obj_categoria.categoria, "Europa")
        self.assertEqual(self.categoria.delete_categoria(1), 200)
        self.assertEqual(self.categoria.read_categoria(1), 404)
        # --------------------------------------------------------------------------------------------------------------
        dados = {'categoria': "Brasileirão"}
        self.assertEqual(self.categoria.create_categoria(dados), 200)
        dados_sub = {'descricao': "Corinthians", 'categoria': self.categoria.obj_categoria}

        '''Teste criar subcategoria'''
        self.assertEqual(self.subcategoria.create_subcategoria(dados_sub), 200)
        self.assertEqual(self.subcategoria.create_subcategoria(dados_erro), 300)

        '''Teste buscar subcategoria'''
        self.assertEqual(self.subcategoria.read_subcategoria(1), 200)
        self.assertEqual(self.subcategoria.read_subcategoria(2), 404)
        self.assertEqual(self.subcategoria.read_subcategoria(dados_erro), 300)
        self.assertEqual(self.subcategoria.obj_subcategoria.categoria_fk.categoria, "Brasileirão")
        self.assertEqual(self.subcategoria.obj_subcategoria.descricao, "Corinthians")

        '''Carrega nova categoria para teste'''
        dados = {'categoria': "Europa"}
        self.assertEqual(self.categoria.create_categoria(dados), 200)
        self.categoria.read_categoria(3)
        dados_sub = {'descricao': "Bayern", 'categoria': self.categoria.obj_categoria}

        '''Teste atualizar subcategoria'''
        self.assertEqual(self.subcategoria.update_subcategoria(1, dados_sub), 200)
        self.assertEqual(self.subcategoria.update_subcategoria(1, dados_erro), 300)
        self.assertEqual(self.subcategoria.obj_subcategoria.descricao, "Bayern")

        '''Teste delete subcategoria'''
        self.assertEqual(self.subcategoria.delete_subcategoria(1), 200)
        self.assertEqual(self.subcategoria.read_subcategoria(1), 404)














