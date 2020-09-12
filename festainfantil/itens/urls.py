from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:id>', views.adicionar, name='item_adicionar'),
    path('imagem/<int:id>', views.imagem, name='item_imagem'),
    path('editar/<int:id>', views.editar, name='item_editar'),
    path('deletar/<int:id>', views.deletar, name='item_deletar'),
]
