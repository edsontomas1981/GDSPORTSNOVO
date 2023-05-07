from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from django.http import JsonResponse
import json

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data['login']
        password = data['senha']

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return JsonResponse({'success': 'True'})
        else:
            return JsonResponse({'success': False, 'error': 'Usuário ou senha incorretos.'})
    
    else:
        return JsonResponse({'status': False, 'error': 'Metodo invalido.'})
