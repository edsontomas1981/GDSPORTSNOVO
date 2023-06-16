from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from checkout import views as views_checkout

urlpatterns = [
    path('',views_checkout.checkout,name='checkout'),
    ]