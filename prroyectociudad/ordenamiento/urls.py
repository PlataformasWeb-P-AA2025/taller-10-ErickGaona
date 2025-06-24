# Este archivo debe ser creado dentro de la carpeta 'ordenamiento'
from django.urls import path
from . import views


# urlpatterns específicos para la aplicación 'ordenamiento'
urlpatterns = [
    # Cuando el usuario vaya a /ordenamiento/, se mostrará la lista de parroquias.
    # Esta es la página principal de la aplicación.
    path('listar_parroquias', views.listar_parroquias, name='listar_parroquias'),
    
    # Ruta para la lista de barrios: /ordenamiento/barrios/
    path('barrios/', views.listar_barrios,name='listar_barrios'),
    
    # Ruta para el formulario de creación de parroquias: /ordenamiento/parroquias/crear/
    path('parroquias/crear/', views.crear_parroquia, name='crear_parroquia'),
    
    # Ruta para el formulario de creación de barrios: /ordenamiento/barrios/crear/
    path('barrios/crear/', views.crear_barrios, name='crear_barrios'),
]
