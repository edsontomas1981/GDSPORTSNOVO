from django.contrib import admin
from loja.models.dados_loja import Dados_loja
from loja.models.menus import Menus

# Register your models here.
admin.site.register(Dados_loja)
admin.site.register(Menus)