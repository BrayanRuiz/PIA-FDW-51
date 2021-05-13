from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name="index"),
    path('acerca-de', views.about, name="about"),
    path('productos', views.productos, name="productos"),
    path('contacto', views.contacto, name="contacto"),
]