from django import forms
from .models import Tablon, Recuerdo

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