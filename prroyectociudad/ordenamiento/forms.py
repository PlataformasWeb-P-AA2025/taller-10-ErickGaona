# Generar un formulario que cree una parroquia

from django.forms import ModelForm
from ordenamiento.models import Parroquia, BarrioCiudadela


class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']
        
        


class BarrioCiudadelaForm(ModelForm):
    class Meta:
        model = BarrioCiudadela
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios_residenciales', 'parroquia']