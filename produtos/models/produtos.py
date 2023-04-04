from django.db import models
from produtos.models.categoria import Categoria
from produtos.models.subcategoria import Subcategoria


class Produtos(models.Model):
    categoria_fk = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=True)
    subcategoria_fk = models.ForeignKey(Subcategoria, on_delete=models.CASCADE, blank=False, null=True)
    descricao = models.CharField(max_length=30, null=True)
    marca = models.CharField(max_length=30, null=True)
    preco = models.FloatField(null=True)
    cor = models.CharField(max_length=30, null=True)
    tamanho = models.CharField(max_length=30, null=True)
    obs = models.CharField(max_length=30, null=True)
