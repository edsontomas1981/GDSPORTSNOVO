from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from loja import views as views_loja

urlpatterns = [
    path('',views_loja.home_loja,name='views_home_loja'),
    # path('adiciona_carrinho',views_carrinho.adiciona_carrinho,name='views_adiciona_carrinho'),
    # path('adiciona_carrinho',views_carrinho.adiciona_carrinho,name='views_adiciona_carrinho'),
    ]