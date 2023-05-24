from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from lista_desejos import views as views_lista_desejos

urlpatterns = [
    path('',views_lista_desejos.lista_desejos,name='views_lista'),
    # path('adiciona_carrinho',views_carrinho.adiciona_carrinho,name='views_adiciona_carrinho'),
    # path('adiciona_carrinho',views_carrinho.adiciona_carrinho,name='views_adiciona_carrinho'),
    ]