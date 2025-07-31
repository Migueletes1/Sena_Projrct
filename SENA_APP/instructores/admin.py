from django.contrib import admin
from django.contrib import admin
from .models import Instructor


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = [
        "documento_identidad",
        "nombre_completo",
        "especialidad",
        "nivel_educativo",
        "anos_experiencia",
        "activo",
        "fecha_registro",
    ]

    list_filter = [
        "nivel_educativo",
        "activo",
        "tipo_documento",
        "especialidad",
        "fecha_vinculacion",
    ]

    search_fields = [
        "nombre",
        "apellido",
        "documento_identidad",
        "correo",
        "especialidad",
    ]

    readonly_fields = ["fecha_registro"]

    fieldsets = (
        (
            "Información Personal",
            {
                "fields": (
                    ("documento_identidad", "tipo_documento"),
                    ("nombre", "apellido"),
                    "fecha_nacimiento",
                    ("correo", "telefono"),
                    ("ciudad", "direccion"),
                )
            },
        ),
        (
            "Información Profesional",
            {
                "fields": (
                    "especialidad",
                    "nivel_educativo",
                    "anos_experiencia",
                    "fecha_vinculacion",
                    "activo",
                )
            },
        ),
        (
            "Información del Sistema",
            {"fields": ("fecha_registro",), "classes": ("collapse",)},
        ),
    )

    date_hierarchy = "fecha_registro"

    def nombre_completo(self, obj):
        return obj.nombre_completo()

    nombre_completo.short_description = "Nombre Completo"
