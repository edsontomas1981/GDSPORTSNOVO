from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from autenticacao import views as views_autenticacao

urlpatterns = [
    path('logado/', views_autenticacao.logado,name='views_logado'),
    path('login/', views_autenticacao.login_view,name='views_login'),
    path('login_fire/', views_autenticacao.login_fire,name='views_fire'),
    path('logout/', views_autenticacao.logout_view,name='views_logout'),
    ]