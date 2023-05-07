from django.shortcuts import redirect
from django.http import JsonResponse
from autenticacao.control.usuarios import Usuarios
from utils import valida_email,checa_campos_vazios,validar_senha
import json

def criar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        campos_obrigatorios=['login','cadastroSenha']
        print(validar_senha(data['cadastroSenha']))
        if valida_email(data['login']):
            return JsonResponse({'status': 'POST'})    
        else:    
            return JsonResponse({'status': 'GET'})    
    else:
        return redirect('/home/')