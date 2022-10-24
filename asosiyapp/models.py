from django.db import models


from userapp.models import Sotuvchi


class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    qarz = models.IntegerField(default=0)
    sotuvchi  = models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL,null=True)
    def __str__(self):return f"{self.ism}, {self.nom}"


class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    narx = models.PositiveIntegerField()
    miqdor =models.FloatField()
    kelgan_sana = models.DateTimeField(auto_now=True)
    olchov = models.CharField(max_length=20)
    sotuvchi = models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL,null=True)
    def __str__(self):return f"{self.brend}, {self.nom}"

