from django.db import models
from asosiyapp.models import *

class Stats(models.Model):
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.SET_NULL,null=True)
    mijoz = models.ForeignKey(Mijoz,on_delete=models.SET_NULL,null=True)
    miqdor = models.FloatField()
    sana = models.DateTimeField(auto_now=True)
    sotuvchi = models.ForeignKey(Sotuvchi,on_delete=models.SET_NULL,null=True)
    jami = models.FloatField()
    tolandi = models.FloatField()
    nasiya = models.FloatField()
    def __str__(self):return f"{self.mahsulot}, {self.mijoz}, {self.jami}"
