from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from produtos.models.categoria import Categoria
import json

# @login_required(login_url='/auth/entrar/')
def read_categorias (request):
    if request.method == 'GET':
        return render(request, 'adiciona_produtos.html')
    elif request.method == "POST" :
        categorias=Categoria.objects.all()
        categorias_dict = [categoria.to_dict() for categoria in categorias]
        return JsonResponse({'categorias':categorias_dict})