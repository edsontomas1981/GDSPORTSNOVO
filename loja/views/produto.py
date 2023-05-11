from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

def produto_loja (request):
    if request.method == 'GET':
        return render(request, 'produtos.html')
    elif request.method == "POST" :
        # data = json.loads(request.body.decode('utf-8'))
        
        return render(request, 'produtos.html')
