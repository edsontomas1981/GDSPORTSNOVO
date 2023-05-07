from django.db import models


class Categoria(models.Model):
    categoria=models.CharField(null=False,max_length=50)  
    subcategorias = models.ManyToManyField('Subcategoria', blank=True)
  
    
    def __str__(self):
        return self.categoria

    def to_dict(self):
        return{'id':self.id,'categoria':self.categoria}