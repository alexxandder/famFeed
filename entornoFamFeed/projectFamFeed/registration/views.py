from django.urls import reverse_lazy
from .forms import UsuarioCrearForm
from django.views.generic import CreateView


# Create your views here.
class RegistroView(CreateView):
    form_class = UsuarioCrearForm
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login')
    
    def get_form(self, form_class=None):
        form = super(RegistroView, self).get_form()
        return form