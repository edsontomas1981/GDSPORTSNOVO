from django.test import TestCase
from produtos.control.categoria import Categoria
from produtos.control.subcategoria import Subcategoria

class Categoria_test(TestCase):
    def setUp(self):
        self.categoria=Categoria()
        self.subcategoria=Subcategoria()
                    
    def test_calculaFrete(self):
        dados={'categoria':"Brasileirão"}
        self.assertEqual(self.categoria.create_categoria(dados),200)
        self.assertEqual(self.categoria.read_categoria(1),200)
        self.assertEqual(self.categoria.read_categoria(2),404)
        dados={'categoria':"Europa"}
        self.assertEqual(self.categoria.update_categoria(1,dados),200)
        self.assertEqual(self.categoria.obj_categoria.categoria,"Europa")
        dadoSub={'descricao':"Bayern",'categoria':self.categoria.obj_categoria}
        self.assertEqual(self.subcategoria.create_subcategoria(dadoSub),200)
        self.assertEqual(self.subcategoria.obj_subcategoria.descricao,"Bayern")
        self.assertEqual(self.subcategoria.obj_subcategoria.categoria_fk.categoria,"Europa")
        self.assertEqual(self.subcategoria.read_subcategoria(1),200)
        
        dadoSub={'descricao':"Bayern",'categoria':self.categoria.obj_categoria}
        self.assertEqual(self.categoria.update_categoria(1,dados),200)
        self.assertEqual(self.subcategoria.obj_subcategoria)

        self.assertEqual(self.categoria.delete_categoria(1),200)
        self.assertEqual(self.categoria.read_categoria(1),404)








