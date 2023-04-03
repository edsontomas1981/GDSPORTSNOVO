from django.db import models
from produtos.models.categoria import Categoria

class Subcategoria(models.Model):
    descricao=models.CharField(null=False,max_length=50)
    categoria_fk=models.ForeignKey(Categoria,on_delete=models.CASCADE, blank=False,
                                    related_name='categoria_fk', null=True)
    
