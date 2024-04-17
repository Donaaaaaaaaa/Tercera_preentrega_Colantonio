from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('insertar/', views.insertar_datos, name='insertar_datos'),
    path('buscar/', views.buscar, name='buscar'),
    # Define otras URLs según sea necesario
]

from django.urls import path, include

urlpatterns = [
    path('mi_aplicacion/', include('mi_aplicacion.urls')),
    # Define otras URLs del proyecto si las hay
]