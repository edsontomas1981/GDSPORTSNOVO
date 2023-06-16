from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from pedidos import views as views_pedidos

urlpatterns = [
    path('',views_pedidos.pedidos,name='pedidos'),
    ]