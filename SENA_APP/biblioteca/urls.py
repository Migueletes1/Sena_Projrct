from django.urls import path
from . import views

app_name = "biblioteca"
urlpatterns = [
    path("materiales/", views.lista_materiales, name="lista_materiales"),
    path("material/<int:pk>/", views.detalle_material, name="detalle_material"),
    path("materiales/agregar/", views.agregar_material, name="agregar_material"),
]
