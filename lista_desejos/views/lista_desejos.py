from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from produtos.control.produtos import Produtos
from lista_desejos.controller.lista_desejos import Lista_desejos

import json

@login_required(login_url='/auth/entrar/')
def lista_desejos (request):
    if request.method == 'GET':
        return JsonResponse({'status':'status_listadesejos','rotas':'rotas_listadesejos'})
    elif request.method == "POST" :
        user = request.user
        data = json.loads(request.body.decode('utf-8'))
        lista = Lista_desejos()
        lista.read_lista(user.id)
        produto=Produtos()
        produto.read_produto_id(data['produtoId'])
        print(produto.obj_produto.to_dict())
        return JsonResponse({'status':'status','rotas':'rotas'})