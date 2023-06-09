from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.decorators.cache import never_cache
from .models import *
from .forms import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


@never_cache
def logout_view(request):
    logout(request)
    return redirect('login')

class TablonListView(LoginRequiredMixin, ListView):
    login_url = 'cuentas/login'
    model = Tablon
    success_url = reverse_lazy('principal')

    def get_queryset(self):
        queryset = super().get_queryset()
        usuario_actual = self.request.user
        queryset = queryset.filter(usuarios=usuario_actual)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tablones'] = self.get_queryset()
        return context
    
class TablonCreateView(LoginRequiredMixin, CreateView):

    login_url = 'cuentas/login'
    model = Tablon
    form_class = newTablonForm
    success_url = reverse_lazy('principal')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        # Guardar el tablón y establecer la relación con el usuario
        tablon = form.save()
        tablon.usuarios.add(self.request.user)
        return super().form_valid(form)
    
class TablonDetailView(LoginRequiredMixin, DetailView):
    model = Tablon
    context_object_name = 'tablon'
    login_url = 'cuentas/login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tablon = self.get_object()
        context['recuerdos'] = tablon.recuerdos.all()
        return context

class AgregarUsuarioTablonView(LoginRequiredMixin, TemplateView):

    template_name = 'agregar_usuario_tablon.html'
    
    def post(self, request, pk):
        try:
            tablon = get_object_or_404(Tablon, pk=pk)
            username = request.POST.get('nombre')
            user = get_object_or_404(User, username=username)
            # Agregar el usuario al tablón utilizando el campo ManyToManyField
            tablon.usuarios.add(user)
            return redirect('detalle', pk=tablon.pk)
        except:
            return self.get(request, pk=tablon.pk)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega los datos adicionales al contexto
        tablon_id = kwargs['pk']
        tablon = Tablon.objects.get(id=tablon_id)
        context['tablon'] = tablon
        return context
    
class RecuerdoCreateView(LoginRequiredMixin, CreateView):

    login_url = 'cuentas/login'
    model = Recuerdo
    form_class = newRecuerdoForm
    success_url = reverse_lazy('principal')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        tablon_id = self.kwargs['pk']
        form.instance.tablon_id = tablon_id 
        recuerdo = form.save()
        return super().form_valid(form)