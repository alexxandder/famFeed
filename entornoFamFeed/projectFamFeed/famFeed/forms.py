from django import forms
from .models import Tablon

class newTablonForm(forms.ModelForm):
    class Meta :
        model = Tablon
        fields = ['nombre', 'imagen']
        labels = {
            'nombre' : 'Título del tablón',
            'imagen' : 'Imagen del tablón'
        }