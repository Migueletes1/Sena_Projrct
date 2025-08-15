from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "biblioteca"
urlpatterns = [
    path("materiales/", views.lista_materiales, name="lista_materiales"),
    path("material/<int:pk>/", views.detalle_material, name="detalle_material"),
    path("materiales/agregar/", views.agregar_material, name="agregar_material"),
]
