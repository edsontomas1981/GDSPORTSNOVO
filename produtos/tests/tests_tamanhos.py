from django.test import TestCase
from produtos.control.tamanho import Tamanhos

class Tamanhos_test(TestCase):
    def setUp(self) -> None:
        self.tamanho = Tamanhos()

    def test_tamanho(self):
        dados={'tamanho':'GG'}
        dados_errados={}
        self.assertEqual(self.tamanho.create_tamanho(dados),200)
        self.assertEqual(self.tamanho.create_tamanho(dados_errados),300)

        self.assertEqual(self.tamanho.read_tamanho(1),200)
        self.assertEqual(self.tamanho.read_tamanho(2),404)
        self.assertEqual(self.tamanho.read_tamanho(dados_errados),300)

        dados={'tamanho':'XG'}
        self.assertEqual(self.tamanho.update_tamanho(1,dados),200)
        self.assertEqual(self.tamanho.update_tamanho(2,dados),404)
        self.assertEqual(self.tamanho.update_tamanho(1,dados_errados),300)
        self.assertEqual(self.tamanho.obj_tamanho.tamanho,'XG')

        self.assertEqual(self.tamanho.delete_tamanho(2),404)
        self.assertEqual(self.tamanho.delete_tamanho(dados_errados),300)
        self.assertEqual(self.tamanho.delete_tamanho(1),200)
        
        


        