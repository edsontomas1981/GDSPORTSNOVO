from django.db import models
from produtos.models.categoria import Categoria

class Subcategoria(models.Model):
    descricao=models.CharField(null=False,max_length=50)
    categoria_fk = models.ManyToManyField('Categoria', blank=True)
    subcategoria_mae = models.ForeignKey('self', null=True, blank=True, related_name='subcategorias', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'subcategorias'
    
    def __str__(self):
        return f'{self.categoria_fk} : {self.descricao}'

    def to_dict(self):
        categorias = list(self.categoria_fk.values())
        subcategoria_mae_id = self.subcategoria_mae.id if self.subcategoria_mae else None
        return {
            'id': self.id,
            'descricao': self.descricao,
            'categoria_fk': categorias,
            'subcategoria_mae': subcategoria_mae_id,
        }
    
