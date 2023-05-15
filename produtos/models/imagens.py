from django.db import models
from produtos.models.produtos import Produtos

class Imagens(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='imagens/')

    class Meta:
        verbose_name_plural = 'Imagens'

    def __str__(self):
        return f"{self.nome} ({self.produto.descricao})"

    def to_dict(self):
        return {
            'id': self.id,
            'produto': self.produto.id,
            'nome': self.nome,
            'imagem': self.imagem.url if self.imagem else None
        }    