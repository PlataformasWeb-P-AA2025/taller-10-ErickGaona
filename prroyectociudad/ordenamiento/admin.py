from django.contrib import admin
from .models import Parroquia, BarrioCiudadela

# --- Personalización del sitio de Administración de Django ---

admin.site.site_header = "Administración de Ordenamiento Territorial"
admin.site.site_title = "Portal de Administración"
admin.site.index_title = "Bienvenido al portal de administración"

# --- Configuración avanzada del Admin ---

# Definimos una clase "Inline" para los barrios.
# Esto nos permitirá ver y agregar barrios directamente desde la página de una parroquia.
class BarrioCiudadelaInline(admin.TabularInline):
    model = BarrioCiudadela
    extra = 1  # Número de formularios extra para agregar barrios
    verbose_name = "Barrio/Ciudadela"
    verbose_name_plural = "Barrios/Ciudadelas"

# Definimos la clase de administración para el modelo Parroquia
class ParroquiaAdmin(admin.ModelAdmin):
    """
    Personaliza la vista de administración para las Parroquias.
    """
    # Incluimos el inline de barrios para una gestión integrada
    inlines = [BarrioCiudadelaInline]
    
    # Campos que se mostrarán en la lista de parroquias
    list_display = ('nombre', 'tipo', 'ubicacion', 'get_total_barrios')
    
    # Filtros que aparecerán en la barra lateral
    list_filter = ('tipo',)
    
    # Habilitar un campo de búsqueda
    search_fields = ('nombre',)

    # Método para contar cuántos barrios tiene cada parroquia
    def get_total_barrios(self, obj):
        return obj.barrios.count()
    
    get_total_barrios.short_description = 'Número de Barrios'

# Definimos la clase de administración para el modelo BarrioCiudadela
class BarrioCiudadelaAdmin(admin.ModelAdmin):
    """
    Personaliza la vista de administración para los Barrios/Ciudadelas.
    """
    # Campos que se mostrarán en la lista de barrios
    list_display = ('nombre', 'parroquia', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales')

    # Filtros
    list_filter = ('parroquia',)

    # Búsqueda
    search_fields = ('nombre', 'parroquia__nombre')

# Registramos los modelos con sus clases de administración personalizadas.
# Si un modelo ya estaba registrado, es buena práctica desregistrarlo primero, aunque no es estrictamente necesario.
# admin.site.unregister(Parroquia) # Descomentar si da problemas de registro duplicado
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(BarrioCiudadela, BarrioCiudadelaAdmin)

