from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

# @login_required(login_url='/auth/entrar/')
def pedidos (request):
    if request.method == 'GET':
        return JsonResponse({'categorias':'pedido_dict'})
    elif request.method == "POST" :
        data = json.loads(request.body.decode('utf-8'))
        return JsonResponse({'categorias':'pedido_dict'})