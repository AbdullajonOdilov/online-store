from django.shortcuts import render, redirect
from django.views import View

from .models import *
from userapp.models import *


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
    def post(self,request):
        Mahsulot.objects.create(
            nom=request.POST.get('pr_name'),
            brend=request.POST.get('pr_brand'),
            narx=request.POST.get('pr_price'),
            miqdor=request.POST.get('pr_amount'),
            kelgan_sana=request.POST.get('pr_date'),
            olchov=request.POST.get('pr_ol'),
            sotuvchi=Sotuvchi.objects.filter(user=request.user)[0]
        )
        return redirect('/sections/mahsulotlar/')

class ProductDeleteView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            now = Sotuvchi.objects.get(user=request.user)
            m = Mahsulot.objects.get(id=pk)
            if m.sotuvchi == now and request.user.is_staff:
                m.delete()
            return redirect('/sections/mahsulotlar/')
        return redirect('login')
class ClientView(View):
    def get(self,request):
        if request.user.is_authenticated:
            info = {
                'clients':Mijoz.objects.filter(sotuvchi__user = request.user)
            }
            return render(request,'clients.html',info)
    def post(self,request):
        Mijoz.objects.create(
            ism=request.POST.get('client_name'),
            nom=request.POST.get('client_shop'),
            manzil=request.POST.get('client_address'),
            tel=request.POST.get('client_phone'),
            qarz=request.POST.get('client_dept'),
            sotuvchi=Sotuvchi.objects.filter(user=request.user)[0]
        )
        return redirect('/sections/clientlar/')
class ClientDeleteView(View):
    def get(self,request,pk):
        if request.user.is_authenticated:
            new = Sotuvchi.objects.get(user=request.user)
            c = Mijoz.objects.get(id=pk)
            if c.sotuvchi == new and request.user.is_staff:
                c.delete()
            return redirect('/sections/clientlar/')
        return redirect('login')

class ClientUpdateView(View):
    def get(self,request,pk):
        now = Sotuvchi.objects.get(user=request.user)

        if request.user.is_authenticated and now == Mijoz.objects.get(id =pk).sotuvchi:
            data = {
            'client': Mijoz.objects.get(id=pk)
            }
            return render(request,'client_update.html',data)
        else:
            return redirect('/sections/clientlar/')
        # return redirect('login')


    def post(self,request,pk):
        Mijoz.objects.filter(id=pk).update(
            ism=request.POST.get('client_name'),
            nom=request.POST.get('client_shop'),
            manzil=request.POST.get('client_address'),
            tel=request.POST.get('client_phone'),
            qarz=request.POST.get('client_dept'),
        )
        return redirect('/sections/clientlar/')

class ProductUpdateView(View):
    def get(self,request,pk):
        hozirgi_ombor = Sotuvchi.objects.get(user=request.user)
        product = Mahsulot.objects.get(id=pk)
        if request.user.is_authenticated and hozirgi_ombor == product.sotuvchi:
            data = {
                'product': Mahsulot.objects.get(id=pk)
            }
            return render(request,'product_update.html',data)
        else:
            return redirect('/sections/mahsulotlar/')
    def post(self,request,pk):
        Mahsulot.objects.filter(id=pk).update(
            nom=request.POST.get('name'),
            brend=request.POST.get('brand'),
            narx=request.POST.get('price'),
            miqdor=request.POST.get('amount'),

            olchov=request.POST.get('ol')
        )
        return redirect('/sections/mahsulotlar/')

