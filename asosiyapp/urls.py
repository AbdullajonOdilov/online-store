from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/',MahsulotlarView.as_view(),name='mahsulotlar'),
    path('clientlar/',ClientView.as_view(),name='clientlar'),
    path('pr_delete/<int:pk>/',ProductDeleteView.as_view(),name ='m-ochir'),
    path('c_delete/<int:pk>/',ClientDeleteView.as_view()),
    path('c_update/<int:pk>/',ClientUpdateView.as_view()),
    path('pr_update/<int:pk>/',ProductUpdateView.as_view()),

]