from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from produtos import views as views_produtos

urlpatterns = [
    path('',views_produtos.produtos,name='views_produtos'),
    ]