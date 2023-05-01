from django.test import TestCase
from lista_desejos.controller.lista_desejos import Lista_desejos

class Lista_desejos_test(TestCase):
    def setUp(self) -> None:
        self.lista_desejos=Lista_desejos()

    def tearDown(self) -> None:
        self.lista_desejos=None
        
    def test_lista_desejos(self):
        dados_errados={}
        # teste cria lista
        self.assertEqual(self.lista_desejos.create_lista_desejos([]),200)
