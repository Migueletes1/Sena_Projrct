from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from .models import Programa
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import Programa
from .forms import ProgramaForm

# Create your views here.
def programas(request):
    lista_programas = Programa.objects.all()
    template = loader.get_template("lista_programas.html")
    context = {
        "lista_programas": lista_programas,
        "total_programas": lista_programas.count(),
    }
    return HttpResponse(template.render(context, request))


def instructores(request):
    """Vista principal para mostrar la lista de instructores con funcionalidad de búsqueda"""
    query = request.GET.get("q")

    if query:

        lista_instructores = Programa.objects.filter(
            Q(nombre__istartswith=query)  # Cambiado de __icontains a __istartswith
            | Q(apellido__istartswith=query)  # Cambiado de __icontains a __istartswith
            | Q(
                documento_identidad__istartswith=query
            )  # Cambiado de __icontains a __istartswith
            | Q(
                especialidad__istartswith=query
            )  # Cambiado de __icontains a __istartswith
        ).order_by("nombre")
    else:
        # Si no hay término de búsqueda, muestra todos los instructores
        lista_instructores = Programa.objects.all().order_by("nombre")

    template = loader.get_template("instructores/lista_instructores.html")
    context = {
        "lista_instructores": lista_instructores,
        "total_instructores": lista_instructores.count(),
    }
    return HttpResponse(template.render(context, request))


def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id)
    cursos = programa.curso_set.all().order_by('-fecha_inicio')
    template = loader.get_template('detalle_programa.html')
    
    context = {
        'programa': programa,
        'cursos': cursos,
    }
    
    return HttpResponse(template.render(context, request))


class ProgramaCreateView(generic.CreateView):
    model = Programa
    form_class = ProgramaForm
    template_name = 'agregar_programa.html'
    success_url = reverse_lazy('programas:lista_programas')