from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tema_index'),
    path('adicionar/', views.adicionar, name='tema_adicionar'),
    path('editar/<int:id>', views.editar, name='tema_editar'),
]
