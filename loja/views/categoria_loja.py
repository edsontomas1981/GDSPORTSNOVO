from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from produtos.models.produtos import Produtos
from loja.controller import subcategorias_por_menu,buscar_quantidade_produtos_por_marca
import json

def categoria_loja (request):
    if request.method == 'GET':      
        return render(request,'categoria.html') 
    elif request.method == "POST" :
        data = json.loads(request.body.decode('utf-8'))
        marcas_dict=buscar_quantidade_produtos_por_marca()
        subcategorias=subcategorias_por_menu(data['idMenu'])
        if data['idMenu']:
            produtos = [produto for produto in Produtos.objects.all() if produto.categoria_fk.menu.id == int(data['idMenu'])]
            produtos_dict = [produto.to_dict() for produto in produtos]
        else:
            produtos = [produto for produto in Produtos.objects.all()]
            produtos_dict = [produto.to_dict() for produto in produtos]
        return JsonResponse({'status': produtos_dict,
                             'subcategorias':subcategorias,
                             'marcas':marcas_dict})
    

