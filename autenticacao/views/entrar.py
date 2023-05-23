from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json

def entrar(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data['login']
        password = data['senha']

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            user_data = {'id':user.id,
                         'username':user.username}
            return JsonResponse({'status': 200 ,'usuario':user_data})
        else:
            return JsonResponse({'status': 404, 'error': 'Usuário ou senha incorretos.'})
    
    else:
        return JsonResponse({'status': 405, 'error': 'Metodo inválido.'})
