from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:id>', views.adicionar, name='item_adicionar'),
]
