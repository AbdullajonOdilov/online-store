from django.shortcuts import render
from django.views import View

from .models import *


class BolimlarView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')

class MahsulotlarView(View):

    def get(self,request):
        if request.user.is_authenticated:
            data = {
                'mahsulotlar':Mahsulot.objects.filter(sotuvchi__user = request.user)
            }
            return render(request,'products.html', data)


class ClientView(View):
    def get(self,request):
        if request.user.is_authenticated:
            info = {
                'clients':Mijoz.objects.filter(sotuvchi__user = request.user)

            }
            return render(request,'clients.html',info)

