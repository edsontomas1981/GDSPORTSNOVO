from django.db import models
from produtos.models.categoria import Categoria
from produtos.models.subcategoria import Subcategoria
from produtos.models.cores import Cores
from produtos.models.tamanhos import Tamanhos
from produtos.models.marca import Marcas

class Produtos(models.Model):
    categoria_fk = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=True)
    subcategoria_fk = models.ManyToManyField(Subcategoria,blank=True)
    descricao = models.CharField(max_length=30, null=True)
    qtde = models.IntegerField(null=True)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE, blank=False, null=True)
    preco = models.FloatField(null=True)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE, blank=False, null=True)
    tamanho = models.ForeignKey(Tamanhos, on_delete=models.CASCADE, blank=False, null=True)
    obs = models.CharField(max_length=30, null=False,blank=True)
    capa = models.ImageField(upload_to='produtos/imagens/capas/', null=False,blank=True)

    class Meta:
        verbose_name_plural = 'Produtos'


    def __str__(self):
        return self.descricao

    def to_dict(self):
        subcategorias = [subcategoria.to_dict() for subcategoria in self.subcategoria_fk.all()]
        return {
            "id": self.id,
            "categoria_fk": self.categoria_fk.to_dict() if self.categoria_fk else None,
            "subcategorias": subcategorias if subcategorias else None, 
            "descricao": self.descricao,
            "qtde": self.qtde,
            "marca": self.marca.to_dict() if self.marca else None,
            "preco": self.preco,
            "cor": self.cor.to_dict() if self.cor else None,
            "tamanho": self.tamanho.to_dict() if self.tamanho else None,
            "obs": self.obs,
            'capa': self.capa.url if self.capa else None,
        }