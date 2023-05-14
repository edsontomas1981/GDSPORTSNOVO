from django.db import models
from produtos.models.produtos import Produtos

class Avaliacoes(models.Model):
    
    nome=models.CharField(null=False,max_length=50)
    email=models.EmailField(null=False)
    avaliacao=models.CharField(null=True,max_length=140)
    estrelas=models.IntegerField()
    produtos = models.ManyToManyField('Produtos', blank=True)

    def __str__(self):
        return self.categoria

    def to_dict(self):
        return{'id':self.id,'categoria':self.categoria,
                "menu": self.menu.to_dict() if self.menu else None,
}