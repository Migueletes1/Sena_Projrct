from django.db import models
from programas.models import Programa
from instructores.models import Instructor  # <-- IMPORTANTE


class Material(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    tipo = models.CharField(
        max_length=50,
        choices=[
            ("PDF", "PDF"),
            ("Word", "Word"),
            ("Excel", "Excel"),
            ("Imagen", "Imagen"),
            ("Otro", "Otro"),
        ],
    )
    palabras_clave = models.TextField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True, blank=True
    )
    archivo = models.FileField(upload_to="materiales/", null=True, blank=True)

    def __str__(self):
        return self.nombre
