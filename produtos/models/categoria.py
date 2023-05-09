from django.db import models
from loja.models.menus import Menus


class Categoria(models.Model):
    categoria=models.CharField(null=False,max_length=50)
    menu=models.ForeignKey(Menus,null=True,blank=True,related_name='menus_categoria', 
                           on_delete=models.CASCADE)  
    subcategorias = models.ManyToManyField('Subcategoria', blank=True)
  
    
    def __str__(self):
        return self.categoria

    def to_dict(self):
        return{'id':self.id,'categoria':self.categoria,
                "menu": self.menu.to_dict() if self.menu else None,
}