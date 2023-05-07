from django.db import models

class Cores(models.Model):
    cor=models.CharField(null=False,max_length=15)

    class Meta:
        verbose_name_plural = 'Cores'
    
    def __str__(self):
        return self.cor
    
    def to_dict(self):
        return{'id':self.id,'cor':self.cor}    