from django.contrib import admin
from produtos.models import Categoria,Cores,Subcategoria,Tamanhos,Imagens,Marcas
from produtos.models.produtos import Produtos
from produtos.models.imagens import Imagens

# Register your models here.
admin.site.register(Produtos)
admin.site.register(Categoria)
admin.site.register(Cores)
admin.site.register(Subcategoria)
admin.site.register(Tamanhos)
admin.site.register(Imagens)
admin.site.register(Marcas)

