from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

def logado (request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == "POST":
        if request.user.is_authenticated:
            return JsonResponse({'status': 200})
        else:
            return JsonResponse({'status': 401, 'message': 'Usuário não autenticado'})