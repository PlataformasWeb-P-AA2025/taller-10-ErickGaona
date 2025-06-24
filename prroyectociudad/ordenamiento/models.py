from django.db import models

# #Dadas dos entidades:

# Parroquia:

#     nombre
#     ubicación (norte, sur, este, oeste)
#     tipo [urbana, rural]

# Barrio o Ciudadela:

#     nombre
#     número de viviendas
#     número de parques [1, 2, 3, 4, 5, 6]
#     número de edificios residenciales
#     parroquia

class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=50)  # norte, sur, este, oeste
    tipo = models.CharField(max_length=10, choices=[('urbana', 'Urbana'), ('rural', 'Rural')])


    def __str__(self):
        return "%s (%s, %s)" % (self.nombre, 
                                self.ubicacion,
                                  self.tipo)


    
    
class BarrioCiudadela(models.Model):
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.PositiveIntegerField()
    numero_parques = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 7)]) 
    numero_edificios_residenciales = models.PositiveIntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE,related_name='barrios')
   


    def __str__(self):
        return "%s (%d viviendas, %d parques, %d edificios)" % (
            self.nombre,
            self.numero_viviendas,
            self.numero_parques,
            self.numero_edificios_residenciales

        )
    

