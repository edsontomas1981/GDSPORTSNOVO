from django.db import models

class Cores(models.Model):
    cor=models.CharField(null=False,max_length=15)
    