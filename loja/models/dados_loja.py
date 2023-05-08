from django.db import models

class Dados_loja(models.Model):
    logo = models.ImageField(upload_to='imagens/logo/')
    whatsapp = models.CharField(max_length=30)
    instagram = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    cnpj_cpf = models.CharField(max_length=18)

    class Meta:
        verbose_name = 'Dados da Loja'
        verbose_name_plural = 'Dados das Lojas'

    def to_dict(self):
        return{'id':self.id,
               'logo':self.logo.url if self.logo else None,
               'whatsapp':self.whatsapp,
               'instagram':self.instagram,
               'fone':self.instagram,
               'cnpj_cpf':self.cnpj_cpf,
                }