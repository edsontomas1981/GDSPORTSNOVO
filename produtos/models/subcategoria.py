from django.db import models
from produtos.models.categoria import Categoria

class Subcategoria(models.Model):
    descricao=models.CharField(null=False,max_length=50)
    categoria_fk = models.ManyToManyField('Categoria', blank=True)

    class Meta:
        verbose_name_plural = 'subcategorias'
    
    def __str__(self):
        return f'{self.categoria_fk} : {self.descricao}'

    def to_dict(self):
        categorias = list(self.categoria_fk.values())
        return {
            'id': self.id,
            'descricao': self.descricao,
            'categoria_fk': categorias,
        }
    
