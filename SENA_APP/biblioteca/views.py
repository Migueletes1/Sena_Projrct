from django.shortcuts import render, get_object_or_404
from .models import Material
from programas.models import Programa
from django.shortcuts import render, redirect
from .forms import MaterialForm

from django.shortcuts import render, get_object_or_404
from .models import Material


def lista_materiales(request):
    query = request.GET.get("q")
    programa_id = request.GET.get("programa")

    materiales = Material.objects.all()
    programas = Programa.objects.all()

    # Filtrar por búsqueda
    if query:
        materiales = materiales.filter(nombre__icontains=query) | materiales.filter(
            palabras_clave__icontains=query
        )

    # Filtrar por programa
    if programa_id:
        materiales = materiales.filter(programa_id=programa_id)

    return render(
        request,
        "biblioteca/lista_materiales.html",
        {"materiales": materiales, "programas": programas},
    )


def detalle_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    return render(request, "biblioteca/detalle_material.html", {"material": material})


def agregar_material(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "biblioteca:lista_materiales"
            )  # <- después de guardar, redirige
    else:
        form = MaterialForm()
        if request.method == "POST":
            form = MaterialForm(request.POST, request.FILES)

    # Siempre devolver algo, incluso si no se envió POST
    return render(request, "biblioteca/agregar_material.html", {"form": form})
