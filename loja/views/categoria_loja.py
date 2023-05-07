from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json
from produtos.models.produtos import Produtos
from produtos.models.imagens import Imagens

def categoria_loja (request):
    if request.method == 'GET':        
        return render(request,'categoria.html')
    elif request.method == "POST" :

        produtos = Produtos.objects.all()
        produtos_dict = [produto.to_dict() for produto in produtos]
        return JsonResponse({'status': produtos_dict})       
