from django.test import TestCase
from autenticacao.control.usuarios import Usuarios


class Autenticacao_test(TestCase):
    def setUp(self) -> None:
        self.usuario=Usuarios()

    def test_autenticacao(self):
        dados={'user':'edson','email':'email@email.com','password':'analu1710'}
        self.usuario.create_user(dados)
        self.assertEqual(self.usuario.user.username,'edson')
        self.assertEqual(self.usuario.entrar('edson','analu110'),300)
        self.assertEqual(self.usuario.entrar('edson','analu1710'),200)
        