from django.db import models

class Menus(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.descricao

    def to_dict(self):
        return{'id':self.id,'descricao':self.descricao,}