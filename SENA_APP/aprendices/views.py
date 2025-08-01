from django.shortcuts import render
from .models import Aprendiz
from django.db.models import Q
from django.http import HttpResponse
from django.template import loader


def inicio_aprendices(request):
    # Corrección: se cambia "-fecha_registro" por "-id" para ordenar por los registros más recientes
    latest_aprendices = Aprendiz.objects.all().order_by("-id")
    context = {"latest_aprendices": latest_aprendices}
    return render(request, "inicio.html", context)


def aprendices(request):
    lista_aprendices = Aprendiz.objects.all()
    return render(request, "lista_aprendices.html", {"aprendices": lista_aprendices})


def aprendices_lista_instructores(request):
    """Vista principal para mostrar la lista de instructores con funcionalidad de búsqueda"""
    query = request.GET.get("q")

    if query:
        # Filtra instructores que COMIENCEN con el término en nombre, apellido, documento o especialidad
        lista_instructores = Aprendiz.objects.filter(
            Q(nombre__istartswith=query)
            | Q(apellido__istartswith=query)
            | Q(documento_identidad__istartswith=query)
            | Q(especialidad__istartswith=query)
        ).order_by("apellido", "nombre")
    else:
        # Si no hay término de búsqueda, muestra todos los instructores
        lista_aprendices = Aprendiz.objects.all().order_by("apellido", "nombre")

    template = loader.get_template("aprendices/lista_aprendices.html")
    context = {
        "lista_aprendices": lista_aprendices,
        "total_aprendices": lista_aprendices.count(),
    }
    return HttpResponse(template.render(context, request))


def inicio(request):
    """Vista de inicio para instructores"""
    total_instructores = Aprendiz.objects.count()
    # Corrección: se cambia "-fecha_registro" por "-id" para ordenar por los registros más recientes
    instructores_recientes = Aprendiz.objects.order_by("-id")[:5]

    context = {
        "total_instructores": total_instructores,
        "instructores_recientes": instructores_recientes,
    }
    return render(request, "inicio.html", context)
    return render(request, "inicio.html", context)
