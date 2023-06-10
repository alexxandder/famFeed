from django import forms
from .models import *

class newComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpo']
        labels = {
            'cuerpo': 'Comentario',
        }

class newTablonForm(forms.ModelForm):
    class Meta :
        model = Tablon
        fields = ['nombre', 'imagen']
        labels = {
            'nombre' : 'Título del tablón',
            'imagen' : 'Imagen del tablón'
        }

class newRecuerdoForm(forms.ModelForm):
    texto = forms.CharField(widget=forms.Textarea(attrs={'rows': 8}))

    class Meta :
        model = Recuerdo
        fields = ['titulo', 'imagenRecuerdo', 'texto', ]
        labels = {
            'titulo' : 'Título del recuerdo',
            'imagenRecuerdo' : 'Imagen del recuerdo',
            'texto' : 'Descripción del recuerdo'
        }