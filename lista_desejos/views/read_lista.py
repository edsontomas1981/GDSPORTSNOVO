from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from produtos.control.produtos import Produtos 
from lista_desejos.controller.lista_desejos import Lista_desejos 
import json

@login_required(login_url='/auth/entrar/')
def read_lista_desejos(request):
    if request.method == 'GET':
        return JsonResponse({'status': 200, 'produtos': listaProdutos})
    elif request.method == "POST":
        user = request.user
        lista=Lista_desejos()
        lista_desejos = lista.read_lista(user)
        listaProdutos = [i.produtos_fk.to_dict() for i in lista_desejos] if lista_desejos is not None else []
        return JsonResponse({'status': 200, 'produtos': listaProdutos})
