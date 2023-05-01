from django.db import models
from autenticacao.control.usuarios import Usuarios 
from produtos.models.produtos import Produtos

class Lista_desejos(models.Model):
    usuario_fk = models.ForeignKey(Usuarios, on_delete=models.CASCADE, blank=False, null=True)
    produtos_fk = models.ManyToManyField(Produtos)
    data = models.DateField()

