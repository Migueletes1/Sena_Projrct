from django import forms
from .models import Aprendiz

class AprendizForm(forms.Form):
    documento_identidad = forms.CharField(
        max_length=100, 
        label="Documento de Identidad",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el documento de identidad'})
    )
    nombre = forms.CharField(
        max_length=100, 
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'})
    )
    apellido = forms.CharField(
        max_length=100, 
        label="Apellido",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'})
    )
    correo = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'})
    )
    telefono = forms.CharField(
        max_length=15, 
        label="Teléfono",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el teléfono'})
    )
    ciudad = forms.CharField(
        max_length=100, 
        label="Ciudad", 
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la ciudad'})
    )
    fecha_nacimiento = forms.DateField(
        label="Fecha de Nacimiento",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )

    def clean(self):
        cleaned_data = super().clean()
        documento_identidad = cleaned_data.get('documento_identidad')
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')
        if not nombre or not apellido or not documento_identidad:
            raise forms.ValidationError("Todos los campos son obligatorios.")
        return cleaned_data

    def clean_documento_identidad(self):
        documento_identidad = self.cleaned_data.get('documento_identidad')
        if documento_identidad is None or not documento_identidad.isdigit():
            raise forms.ValidationError("El campo 'Documento de Identidad' debe ser un número.")
        return documento_identidad

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El campo 'teléfono' debe ser un número.")
        return telefono

    def save(self):
        aprendiz = Aprendiz(
            documento_identidad=self.cleaned_data['documento_identidad'],
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            correo=self.cleaned_data['correo'],
            telefono=self.cleaned_data['telefono'],
            ciudad=self.cleaned_data['ciudad'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento']
        )
        aprendiz.save()
        return aprendiz