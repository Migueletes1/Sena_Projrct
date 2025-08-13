from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'documento_identidad', 'tipo_documento', 'nombre', 'apellido',
            'telefono', 'correo', 'fecha_nacimiento', 'ciudad', 'direccion',
            'nivel_educativo', 'especialidad', 'anos_experiencia',
            'activo', 'fecha_vinculacion'
        ]
        widgets = {
            'documento_identidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el documento de identidad'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección'}),
            'nivel_educativo': forms.Select(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la especialidad'}),
            'anos_experiencia': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Años de experiencia'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_vinculacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }