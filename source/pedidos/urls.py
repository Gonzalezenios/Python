from django.contrib import admin
from django.urls import path
from.views import index, guardar_pedidos




urlpatterns = [
    path('', index),
    path('guardar/', guardar_pedidos),
]