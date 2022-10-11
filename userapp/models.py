from django.contrib.auth.models import User
from django.db import models

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)
    tel = models.CharField(max_length=11)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vazifa = models.CharField(max_length=30,blank=True)
    def __str__(self):return f"{self.ism}, {self.nom}"

