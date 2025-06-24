"""
URL configuration for prroyectociudad project.
"""
from django.contrib import admin
from django.urls import path, include
from ordenamiento import views

urlpatterns = [
    # URLs del sitio de administración
    path('admin/', admin.site.urls),
    path('', include('ordenamiento.urls')),
    
]
