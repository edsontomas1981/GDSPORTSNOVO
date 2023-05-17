from produtos.models.marca import Marcas
from django.db.models import Count

def buscar_quantidade_produtos_por_marca():
    marcas = Marcas.objects.all().annotate(total_registros=Count('produtos'))
    marcas_list = [{'id': marca.id,
                    'marca': marca.marca,
                    'total_registros': marca.total_registros} for marca in marcas]
    return marcas_list