from django.shortcuts import render, redirect
from django.views import View

from .models import Stats
from asosiyapp.models import *


class StatsView(View):
    def get(self, request):
        statslar = Stats.objects.filter(sotuvchi__user=request.user)
        qidiruv_sozi = request.GET.get('soz')
        if qidiruv_sozi is not None:
            statslar = statslar.filter(mahsulot__nom__contains=
            qidiruv_sozi) | statslar.filter(mahsulot__brend__contains=
            qidiruv_sozi) | statslar.filter(mijoz__nom__contains=
            qidiruv_sozi) | statslar.filter(
                mijoz__ism__contains=qidiruv_sozi
            )

        data = {
            'stats': statslar,
            "products":Mahsulot.objects.all(),
            'clients':Mijoz.objects.all()
        }
        return render(request, 'stats.html', data)

    def post(self,request):
        Stats.objects.create(
            mahsulot = Mahsulot.objects.get(id=request.POST.get("product_id")),
            mijoz = Mijoz.objects.get(id = request.POST.get("client_id")),
            sana = request.POST.get("sana"),
            miqdor = request.POST.get("miqdor"),
            sotuvchi = Sotuvchi.objects.get(id=request.POST.get("sotuvchi")),
            jami =request.POST.get("summa"),
            nasiya = request.POST.get("nasiya"),
            tolandi = request.POST.get('tolandi')
        )
        return redirect('/stats/')
