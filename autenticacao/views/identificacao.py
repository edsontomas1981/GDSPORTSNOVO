from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

def identificacao (request):
    if request.method == 'GET': 
        return render(request,'identificacao.html') 
   
    elif request.method == "POST" :
        return render(request,'identificacao.html') 
