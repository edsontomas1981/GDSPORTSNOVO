from django.db import models

class Menus(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def to_dict(self):
        return{'id':self.id,
               'logo':self.logo.url if self.logo else None,
               'whatsapp':self.whatsapp,
               'instagram':self.instagram,
               'fone':self.instagram,
               'cnpj_cpf':self.cnpj_cpf,
                }