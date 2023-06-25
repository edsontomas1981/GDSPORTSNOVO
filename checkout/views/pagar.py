from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

# @login_required(login_url='/autenticacao/identificacao/')
def pagar (request):
    if request.method == 'GET': 
        return render(request,'pagamentos.html') 
   
    elif request.method == "POST" :
        return render(request,'pagamentos.html') 
