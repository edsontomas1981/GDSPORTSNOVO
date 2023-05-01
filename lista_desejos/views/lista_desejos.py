from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

@login_required(login_url='/auth/entrar/')
def lista_desejos (request):
    if request.method == 'GET':
        return JsonResponse({'status':'status_listadesejos','rotas':'rotas_listadesejos'})
    elif request.method == "POST" :
        data = json.loads(request.body.decode('utf-8'))
        return JsonResponse({'status':'status','rotas':'rotas'})