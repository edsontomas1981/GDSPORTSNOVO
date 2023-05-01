from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

@login_required(login_url='/home/')
def carrinho (request):
    if request.method == 'GET':
        return render(request, 'adiciona_produtos.html')
    elif request.method == "POST" :
        data = json.loads(request.body.decode('utf-8'))
        return JsonResponse({'logou':200})