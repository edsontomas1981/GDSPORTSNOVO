from django.contrib import admin
from produtos.models import Produtos,Categoria,Cores,Subcategoria,Tamanhos,Imagens,Marcas

# Register your models here.

admin.site.register(Produtos)
admin.site.register(Categoria)
admin.site.register(Cores)
admin.site.register(Subcategoria)
admin.site.register(Tamanhos)
admin.site.register(Imagens)
admin.site.register(Marcas)

