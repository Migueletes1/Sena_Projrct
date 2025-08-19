# instructores/views.py
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.db.models import Q
from .models import Instructor
from django.shortcuts import render, get_object_or_404
from .forms import InstructorForm
from django.urls import reverse_lazy
from django.views import generic


def instructores(request):
    """Vista principal para mostrar la lista de instructores con funcionalidad de búsqueda"""
    query = request.GET.get("q")

    if query:
        # Filtra instructores que COMIENCEN con el término en nombre, apellido, documento o especialidad
        lista_instructores = Instructor.objects.filter(
            Q(nombre__istartswith=query)  # Cambiado de __icontains a __istartswith
            | Q(apellido__istartswith=query)  # Cambiado de __icontains a __istartswith
            | Q(documento_identidad__istartswith=query)  # Cambiado de __icontains a __istartswith
            | Q(especialidad__istartswith=query)  # Cambiado de __icontains a __istartswith
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
def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id)
    # Use the correct variable name 'instructor' instead of 'instructores'
    cursos_coordinados = instructor.cursos_coordinados.all()
    cursos_impartidos = instructor.cursos_impartidos.all()
    template = loader.get_template('instructores/detalle_instructor.html')
    context = {
        'instructor': instructor,
        'cursos_coordinados': cursos_coordinados,
        'cursos_impartidos': cursos_impartidos,
    }
    return HttpResponse(template.render(context, request))
class InstructorCreateView(generic.CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'instructores/agregar_instructor.html'
    success_url = reverse_lazy('instructores:lista_instructores')
