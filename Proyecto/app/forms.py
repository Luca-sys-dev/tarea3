from django import forms

class ConsecionarioForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=20)

class VehiculoForm(forms.Form):
    marca = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    modelo = forms.CharField(max_length=20)
    patente = forms.CharField(max_length=7)
    valor = forms.IntegerField()
    kilometraje = forms.IntegerField()

class AgenteForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    edad = forms.IntegerField()
    sueldo = forms.IntegerField()

class AgenteBusqueda(forms.Form):
    dni = forms.IntegerField()