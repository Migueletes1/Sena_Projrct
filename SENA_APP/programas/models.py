from django.db import models


# Tu modelo
class Programa(models.Model):
    NIVEL_FORMACION_CHOICES = (
        ("AUX", "Auxiliar"),
        ("GPE", "Operario"),
        ("TEC", "Tecnico"),
        ("TEL", "Tecnologo"),
        ("ESP", "Especialización Tecnológica"),
        ("COM", "Complementario"),
    )

    MODELO_CHOICES = (
        ("PRE", "Pregrado"),
        ("VTI", "Virtual"),
        ("MAX", "Maxtech"),
    )

    ESTADO_CHOICES = (
        ("ACT", "Activo"),
        ("INA", "Inactivo"),
        ("SUS", "Suspendido"),
        ("CAN", "Cancelado"),
    )

    codigo = models.CharField(
        max_length=3, unique=True, verbose_name="Código del Programa"
    )
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Programa")
    nivel_formacion = models.CharField(
        max_length=3, choices=NIVEL_FORMACION_CHOICES, verbose_name="Nivel de Formación"
    )
    modalidad = models.CharField(
        max_length=3, choices=MODELO_CHOICES, verbose_name="Modalidad"
    )
    estado = models.CharField(
        max_length=3, choices=ESTADO_CHOICES, default="ACT", verbose_name="Estado"
    )
    duracion_meses = models.PositiveIntegerField(verbose_name="Duración en Meses")
    duracion_horas = models.PositiveIntegerField(verbose_name="Duración en Horas")
    descripcion = models.TextField(verbose_name="Descripción del Programa")
    competencias = models.TextField(verbose_name="Competencias a Desarrollar")
    perfil_egreso = models.TextField(verbose_name="Perfil de Egreso")
    requisitos_ingreso = models.TextField(verbose_name="Requisitos de Ingreso")
    centro_formacion = models.CharField(
        max_length=200, verbose_name="Centro de Formación"
    )
    regional = models.CharField(max_length=100, verbose_name="Regional")
    fecha_creacion = models.DateField(verbose_name="Fecha de Creación del Programa")
    fecha_registro = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Registro"
    )

    class Meta:
        verbose_name = "Programa de Formación"
        verbose_name_plural = "Programas de Formación"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    def get_duracion_completa(self):
        return f"{self.duracion_meses} meses ({self.duracion_horas} horas)"

    def is_activo(self):
        return self.estado == "ACT"