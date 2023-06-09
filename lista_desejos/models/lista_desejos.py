from django.db import models
from produtos.models import Produtos
from django.contrib.auth.models import User
from datetime import datetime

class Lista_desejos(models.Model):
    usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    produtos_fk = models.ForeignKey(Produtos, on_delete=models.CASCADE, blank=False, null=True)
    data = models.DateField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.data = datetime.now().strftime("%Y-%m-%d")
        super().save(*args, **kwargs)
