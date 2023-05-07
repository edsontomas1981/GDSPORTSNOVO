from django.db import models

class Tamanhos(models.Model):
    tamanho=models.CharField(null=False,max_length=8)

    def __str__(self):
        return self.tamanho

    class Meta:
        verbose_name_plural = 'Tamanhos'
    
    def to_dict(self):
        return{'id':self.id,'tamanho':self.tamanho}