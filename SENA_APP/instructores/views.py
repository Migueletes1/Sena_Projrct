# instructores/views.py
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from .models import Instructor


def instructores(request):
    """Vista principal para mostrar la lista de instructores con funcionalidad de búsqueda"""
    query = request.GET.get("q")

    if query:
        # Filtra instructores que COMIENCEN con el término en nombre, apellido, documento o especialidad
        lista_instructores = Instructor.objects.filter(
            Q(nombre__istartswith=query)  # Cambiado de __icontains a __istartswith
            | Q(apellido__istartswith=query)  # Cambiado de __icontains a __istartswith
            | Q(
                documento_identidad__istartswith=query
            )  # Cambiado de __icontains a __istartswith
            | Q(
                especialidad__istartswith=query
            )  # Cambiado de __icontains a __istartswith
        ).order_by("apellido", "nombre")
    else:
        # Si no hay término de búsqueda, muestra todos los instructores
        lista_instructores = Instructor.objects.all().order_by("apellido", "nombre")

    template = loader.get_template("instructores/lista_instructores.html")
    context = {
        "lista_instructores": lista_instructores,
        "total_instructores": lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))


def inicio(request):
    """Vista de inicio para instructores"""
    total_instructores = Instructor.objects.count()
    instructores_recientes = Instructor.objects.order_by("-fecha_registro")[:5]

    context = {
        "total_instructores": total_instructores,
        "instructores_recientes": instructores_recientes,
    }
    return render(request, "instructores/inicio.html", context)
