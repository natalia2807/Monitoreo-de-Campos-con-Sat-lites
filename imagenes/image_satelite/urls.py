from django.urls import path
from .views import descargar_imagenes,obtener_imagenes_zip

urlpatterns = [
    path('descargar_imagenes/', descargar_imagenes, name='descargar_imagenes'),
    path('obtener_imagenes_zip/', obtener_imagenes_zip, name='obtener_imagenes_zip'),
]
