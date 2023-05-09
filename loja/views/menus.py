from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from loja.models.menus import Menus
import json

def menus_loja (request):
    if request.method == 'GET':      
        menus = Menus.objects.all()
        menus_dict = [menu.to_dict() for menu in menus]
        return JsonResponse({'status': menus_dict})   
    elif request.method == "POST" :
        # data = json.loads(request.body.decode('utf-8'))
        menus = Menus.objects.all()
        menus_dict = [menu.to_dict() for menu in menus]
        return JsonResponse({'status': menus_dict})       
