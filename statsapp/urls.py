from django.contrib import admin
from django.urls import path

from statsapp.views import StatsView

urlpatterns = [
    path('',StatsView.as_view())

]