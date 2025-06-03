from django import forms

class AdminForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre del Administrador", required=True)
    apellido = forms.CharField(max_length=50, label="Apellido del Administrador", required=True)
    email = forms.EmailField(required=True)

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre del Administrador", required=True)
    apellido = forms.CharField(max_length=50, label="Apellido del Administrador", required=True)
    email = forms.EmailField(required=True)
    apodo = forms.CharField(max_length=50, required=True)

class PublicacionesForm(forms.Form):
    titulo_de_publicacion = forms.CharField(max_length=50, label="¿Cual sera el titutlo de la publicacion?", required=True)
    publicacion = forms.CharField(max_length=200, label="Escribi tu posteo", required=True)
    fecha_de_publicacion = forms.DateField(label="¿Qué día es hoy?", required=True, widget=forms.DateInput(attrs={'type': 'date'}))