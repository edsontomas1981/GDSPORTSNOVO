from django.test import TestCase,Client
from django.urls import reverse
from autenticacao.control.usuarios import Usuarios
import json

class Autenticacao_test(TestCase):
    def setUp(self) -> None:
        self.usuario=Usuarios()
        self.client=Client()

    def test_autenticacao(self):
        dados={'user':'edson','email':'email@email.com','password':'analu1710'}
        self.usuario.create_user(dados)

        self.client.login(username='edson', password='analu1710')
        dados = {'chave': 'valor'}
        # Converte o objeto JSON em uma string
        json_dados = json.dumps(dados)
        response = self.client.post('/autenticacao/logado/', 
                                    data=json_dados, content_type='application/json')
        
        # Faz uma requisição POST para a view protegida
        self.assertEqual(response.status_code,200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), 
                             {'logado':'logado'})
        
        self.client.logout()
        # Faz uma solicitação para a view protegida
        response = self.client.post('/autenticacao/logado/')
        # Verifica se a resposta é a esperada
        self.assertEqual(response.status_code, 302) 