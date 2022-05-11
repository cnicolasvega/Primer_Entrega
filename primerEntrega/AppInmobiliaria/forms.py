from django import forms

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    telefono = forms.IntegerField()
    mail = forms.EmailField()

class CasaFormulario(forms.Form):
    direccion = forms.CharField(max_length=200)
    numero = forms.IntegerField()
    pisos = forms.IntegerField()
    habitaciones = forms.IntegerField()
    banos = forms.IntegerField()
    precio = forms.IntegerField()

class DepartamentoFormulario(forms.Form):
    direccion = forms.CharField(max_length=200)
    numero = forms.IntegerField()
    pisos = forms.IntegerField()
    habitaciones = forms.IntegerField()
    banos = forms.IntegerField()
    precio = forms.IntegerField()
    expensas = forms.IntegerField()
