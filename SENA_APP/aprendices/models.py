from django.db import models


class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True)
    correo = models.EmailField(null=True)
    Fecha_nacimiento = models.DateField(null=True)
    ciudad = models.CharField()
    programa = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Aprendiz"
        verbose_name_plural = "Aprendices"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.documento_identidad}"

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    class Curso(models.Model)
    documento_identidad= models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    telefono= models.CharField(max_length=10, null=True)
    correo = models.EmailField(null=True)
    Fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True)
    class Meta:
        verbose_name ="Aprendiz"
        verbose_name_plural="Aprendices"
        ordering = ['apellido','nombre']
        def _str_(self):
            return f"{self.nombre} {self.apellido} - {self.documento_identidad}"
        def nombre_completo(self):
            return f"{self.nombre} {self.apellido}"
        
            

# Create your models here.
