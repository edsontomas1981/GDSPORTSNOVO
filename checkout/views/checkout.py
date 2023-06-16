from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

def checkout (request):
    if request.method == 'GET': 
        return render(request,'checkoutLoja.html') 
   
    elif request.method == "POST" :
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        return render(request,'checkoutLoja.html') 
