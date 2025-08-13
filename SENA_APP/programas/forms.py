from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'codigo', 'nombre', 'nivel_formacion', 'modalidad', 'estado',
            'duracion_meses', 'duracion_horas', 'descripcion', 'competencias',
            'perfil_egreso', 'requisitos_ingreso', 'centro_formacion',
            'regional', 'fecha_creacion'
        ]
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código único'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del programa'}),
            'nivel_formacion': forms.Select(attrs={'class': 'form-control'}),
            'modalidad': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'duracion_meses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en meses'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en horas'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del programa'}),
            'competencias': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Competencias a desarrollar'}),
            'perfil_egreso': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Perfil del egresado'}),
            'requisitos_ingreso': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Requisitos de ingreso'}),
            'centro_formacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del centro de formación'}),
            'regional': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Regional a la que pertenece'}),
            'fecha_creacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }