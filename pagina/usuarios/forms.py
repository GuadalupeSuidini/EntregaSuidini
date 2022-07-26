from socket import fromshare
from django import forms


class EmpleadoFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    fechaNacimiento = forms.DateField()
    email = forms.EmailField()
    dni = forms.IntegerField()


class ClienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    dni = forms.IntegerField()


class ProveedorFormulario(forms.Form):

    cuit = forms.IntegerField()
    razonSocial = forms.CharField()
    email = forms.EmailField()