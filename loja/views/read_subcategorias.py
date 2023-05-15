import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from produtos.models.produtos import Produtos
from django.contrib.auth import authenticate, login


def read_subcategorias (request):
    if request.method == 'GET':      
        pass
    else:
        pass      
