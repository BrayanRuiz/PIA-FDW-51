from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name="index"),
    path('productos', views.productos, name="productos"),
    path('promociones', views.promociones, name="promociones"),
    path('contacto', views.contacto, name="contacto"),
]