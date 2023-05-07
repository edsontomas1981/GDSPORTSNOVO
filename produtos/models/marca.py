from django.db import models

class Marcas(models.Model):
    marca=models.CharField(null=False,max_length=15)
    
    def __str__(self):
        return self.marca

    class Meta:
        verbose_name_plural = 'Marcas'    
    
    def to_dict(self):
        return{'id':self.id,'marca':self.marca}