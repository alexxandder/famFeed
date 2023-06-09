from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', TablonListView.as_view(), name='principal'),
    path('crearTablon/', TablonCreateView.as_view(), name='crearTablon'),
    path('detalle/<int:pk>', TablonDetailView.as_view(), name='detalle'),
    path('agregarUsuarioTablon/<int:pk>', views.AgregarUsuarioTablonView.as_view(), name='agregarUsuarioTablon'),
]