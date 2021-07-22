from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows), # Va a l apagina principal 
    path('shows/new', views.new), # Agrega un nuevo show
    path('shows/<int:id>/edit', views.edit), # Edita un show existente
    path('shows/<int:id>', views.show), # Se ve la información del show
    path('shows/<int:id>/destroy', views.delete), # Elimina un show existente
    
]


