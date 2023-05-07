from django.contrib import admin
# from produtos.models.produtos import Produtos
# from produtos.models.categoria import Categoria
# from produtos.models.cores import Cores
# from produtos.models.subcategoria import Subcategoria
# from produtos.models.tamanhos import Tamanhos
# from produtos.models.imagens import Imagens
# from produtos.models.marca import Marcas
from produtos.models import Produtos,Categoria,Cores,Subcategoria,Tamanhos,Imagens,Marcas


# Register your models here.

admin.site.register(Produtos)
admin.site.register(Categoria)
admin.site.register(Cores)
admin.site.register(Subcategoria)
admin.site.register(Tamanhos)
admin.site.register(Imagens)
admin.site.register(Marcas)

