from django.test import TestCase
from produtos.control.cores import Cores

class Cores_test(TestCase):
    def setUp(self) -> None:
        self.cor = Cores()

    def test_cor(self):
        dados={'cor':'Preta'}
        dados_errados={}
        self.assertEqual(self.cor.create_cor(dados),200)
        self.assertEqual(self.cor.create_cor(dados_errados),300)

        self.assertEqual(self.cor.read_cor(1),200)
        self.assertEqual(self.cor.read_cor(2),404)
        self.assertEqual(self.cor.read_cor(dados_errados),300)

        dados={'cor':'Branca'}
        self.assertEqual(self.cor.update_cor(1,dados),200)
        self.assertEqual(self.cor.update_cor(2,dados),404)
        self.assertEqual(self.cor.update_cor(1,dados_errados),300)
        self.assertEqual(self.cor.obj_cor.cor,'Branca')

        self.assertEqual(self.cor.delete_cor(2),404)
        self.assertEqual(self.cor.delete_cor(dados_errados),300)
        self.assertEqual(self.cor.delete_cor(1),200)
        