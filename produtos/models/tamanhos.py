from django.db import models

class Tamanhos(models.Model):
    tamanho=models.CharField(null=False,max_length=8)