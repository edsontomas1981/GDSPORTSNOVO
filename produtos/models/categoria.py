from django.db import models

class Categoria(models.Model):
    categoria=models.CharField(null=False,max_length=50)
    

