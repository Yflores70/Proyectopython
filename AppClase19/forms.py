from django import forms

class ClienteFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    correo = forms.EmailField(required=True)
    direccion = forms.CharField(required=True)

class AgregaProductoFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)

class AgregaCategoriaFormulario(forms.Form):

    nombre = forms.CharField(required=True)
