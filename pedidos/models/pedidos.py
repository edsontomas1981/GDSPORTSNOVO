from django.db import models
from pedidos.models.endereco import Enderecos
from django.contrib.auth.models import User
from datetime import datetime

class Pedidos(models.Model):
    # Usando cliente mesmo sendo usuario,pra que num momento futuro 
    # possa-se aproveitar essa estrutura dos pedidos 
    cliente_fk = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True) 
    endereco_fk = models.ForeignKey(Enderecos, on_delete=models.CASCADE, blank=False, null=True)
    total_pedido = models.FloatField(null=True)

    data = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.data = datetime.now().strftime("%Y-%m-%d")
        super().save(*args, **kwargs)
