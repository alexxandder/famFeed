from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioCrearForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        correo = self.cleaned_data.get('email')
        if User.objects.filter(email=correo).exists():
            raise forms.ValidationError('Este correo ya está registrado')
        return correo
    