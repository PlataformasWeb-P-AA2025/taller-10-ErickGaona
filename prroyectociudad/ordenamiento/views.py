from django.shortcuts import render, redirect
from .models import Parroquia, BarrioCiudadela
from .forms import ParroquiaForm, BarrioCiudadelaForm

# Vista para listar todas las parroquias y sus barrios asociados
def listar_parroquias(request):
    """
    Esta vista recupera todas las parroquias y barrios de la base de datos
    y las muestra en una plantilla.
    """
    # Usamos prefetch_related para una consulta más eficiente
    parroquias = Parroquia.objects.all().prefetch_related('barrios')
    
    context = {
        'parroquias': parroquias,
    }
    return render(request, 'parroquias_barrios.html', context)

# Vista para listar todos los barrios
def listar_barrios(request):
    """
    Esta vista recupera todos los barrios de la base de datos
    y los muestra en una plantilla.
    """
    barrios = BarrioCiudadela.objects.select_related('parroquia').all()
    
    context = {
        'barrios': barrios,
    }
    return render(request, 'listar_barrios.html', context)

# --- Vistas para crear nuevos registros ---

# Vista para crear una nueva Parroquia
def crear_parroquia(request):
    """
    Esta vista maneja la creación de una nueva parroquia.
    Si el método es POST, procesa el formulario.
    Si es GET, muestra un formulario en blanco.
    """
    if request.method == 'POST':
        # Si se envía el formulario, lo procesamos
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar la nueva parroquia en la base de datos
            return redirect('listar_parroquias') # Redirigir a la lista de parroquias
    else:
        # Si es una petición GET, creamos un formulario vacío
        form = ParroquiaForm()
    
    context = {
        'formulario': form
    }
    return render(request, 'crear_parroquia.html', context)

# Vista para crear un nuevo Barrio/Ciudadela
def crear_barrios(request):
    """
    Esta vista maneja la creación de un nuevo barrio.
    Si el método es POST, procesa el formulario.
    Si es GET, muestra un formulario en blanco.
    """
    if request.method == 'POST':
        form = BarrioCiudadelaForm(request.POST)
        if form.is_valid():
            form.save() # Guardar el nuevo barrio en la base de datos
            return redirect('listar_barrios') # Redirigir a la lista de barrios
    else:
        form = BarrioCiudadelaForm()

    context = {
        'formulario': form
    }
    return render(request, 'crear_barrios.html', context)

