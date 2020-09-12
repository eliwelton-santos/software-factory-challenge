from django.shortcuts import render
from .models import Tema


def index(request):
    temas = Tema.objects.all().order_by('-created_at')
    return render(request, 'temas/index.html', {'temas': temas})
