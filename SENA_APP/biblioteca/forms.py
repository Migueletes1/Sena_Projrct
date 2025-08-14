from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            "nombre",
            "descripcion",
            "tipo",
            "palabras_clave",
            "programa",
            "instructor",
            "archivo",
        ]
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 3}),
            "palabras_clave": forms.Textarea(attrs={"rows": 2}),
        }
