from django.db import models
from produtos.models.categoria import Categoria
from produtos.models.subcategoria import Subcategoria
from produtos.models.cores import Cores
from produtos.models.tamanhos import Tamanhos

class Produtos(models.Model):
    categoria_fk = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=True)
    subcategoria_fk = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, blank=False, null=True)
    descricao = models.CharField(max_length=30, null=True)
    marca = models.CharField(max_length=30, null=True)
    preco = models.FloatField(null=True)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=False, null=True)
    tamanho = models.ForeignKey(Tamanhos, on_delete=models.CASCADE, blank=False, null=True)
    obs = models.CharField(max_length=30, null=True)
