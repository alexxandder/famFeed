from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', TablonListView.as_view(), name='principal'),
    path('crearTablon/', TablonCreateView.as_view(), name='crearTablon'),
    path('detalle/<int:pk>', TablonDetailView.as_view(), name='detalle'),
    path('agregarUsuarioTablon/<int:pk>', views.AgregarUsuarioTablonView.as_view(), name='agregarUsuarioTablon'),
    path('crearRecuerdo/<int:pk>', RecuerdoCreateView.as_view(), name='crearRecuerdo'),
    path('detalleRecuerdo/<int:pk>', RecuerdoDetailView.as_view(), name='detalleRecuerdo'),
    path('eliminarComentario/<int:comentario_id>/', EliminarComentarioView.as_view(), name='eliminarComentario'),
]