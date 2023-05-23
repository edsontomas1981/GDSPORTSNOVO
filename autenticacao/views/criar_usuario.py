from django.shortcuts import redirect
from django.http import JsonResponse
from autenticacao.control.usuarios import Usuarios
from utils import valida_email, checa_campos_vazios, validar_senha
import json

def criar_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
       
        # Verifica se todos os campos foram fornecidos
        if checa_campos_vazios(data, ['login', 'firstName', 'cadastroSenha', 'confirmacaoSenha']):
            return JsonResponse({'status': 400, 'error': 'Todos os campos devem ser preenchidos'})

        # Valida o formato do email
        if not valida_email(data['login']):
            return JsonResponse({'status': 400, 'error': 'Formato de email inválido'})

        # Valida a senha
        if not validar_senha(data['cadastroSenha']):
            return JsonResponse({'status': 400, 'error': 'A senha deve ter pelo menos 8 caracteres e conter letras maiúsculas, minúsculas, números e caracteres especiais'})

        # Verifica se a confirmação de senha coincide
        if data['cadastroSenha'] != data['confirmacaoSenha']:
            return JsonResponse({'status': 400, 'error': 'A confirmação de senha não coincide'})

        # Cria o usuário
        user = Usuarios()
        user.create_user(data)
        return JsonResponse({'status': 200})
    else:
        return redirect('/home/')

    


'''    
    {'login': 'edson@email.com', 
    'firstName': 'Edson Tomas', 
    'cadastroSenha': 'An@lu1710', 
    'confirmacaoSenha': 'An@lu710'}
'''
