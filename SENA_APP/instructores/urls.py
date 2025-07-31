# instructores/urls.py
from django.urls import path
from . import views

app_name = "instructores"  # Necesario para el namespace en las URLs

urlpatterns = [
    path(
        "", views.instructores, name="lista_instructores"
    ),  # Asegúrate de que esta línea exista
    path("inicio/", views.inicio, name="inicio"),
    # ... otras rutas si las tienes
]
