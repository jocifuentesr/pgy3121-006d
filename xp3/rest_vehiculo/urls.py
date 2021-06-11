from django.urls import path
from rest_vehiculo.views import lista_vehiculos

urlpatterns =[
    path('lista_vehiculos', lista_vehiculos, name="lista_vehiculos"),
]