from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from carrinho import views as views_carrinho

urlpatterns = [
    path('',views_carrinho.carrinho,name='views_carrinho'),
    # path('adiciona_carrinho',views_carrinho.adiciona_carrinho,name='views_adiciona_carrinho'),
    # path('adiciona_carrinho',views_carrinho.adiciona_carrinho,name='views_adiciona_carrinho'),
    ]