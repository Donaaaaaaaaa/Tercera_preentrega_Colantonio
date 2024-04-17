from django.shortcuts import render

from .forms import Clase1Form

def insertar_datos(request):
    if request.method == 'POST':
        form = Clase1Form(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página de éxito o renderizar otra vista
    else:
        form = Clase1Form()
    return render(request, 'insertar_datos.html', {'form': form})

from .forms import BusquedaForm
from .models import Clase1, Clase2, Clase3

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino_busqueda']
            # Realizar búsqueda en la base de datos
            resultados = Clase1.objects.filter(campo1__icontains=termino)
            # Puedes hacer lo que quieras con los resultados, como renderizarlos en un template
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar.html', {'form': form})

from django.shortcuts import render

def insertar_datos(request):
    return render(request, 'insertar_datos.html')

def buscar(request):
    return render(request, 'buscar.html')