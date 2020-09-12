from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tema
from .forms import TemaForm


def redirecionar(request):
    return redirect('tema_index')


def index(request):
    temas = Tema.objects.all().order_by('-created_at')
    return render(request, 'temas/index.html', {'temas': temas})


def adicionar(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tema adicionado com sucesso!')
            return redirect('tema_index')
        else:
            messages.warning(request, 'Um ou mais campos foram preenchidos incorretamente!')
            return render(request, 'temas/adicionar.html', {'form': form})
    else:
        form = TemaForm()
        return render(request, 'temas/adicionar.html', {'form': form})


def editar(request, id):
    tema = get_object_or_404(Tema, pk=id)
    form = TemaForm(instance=tema)
    if request.method == 'POST':
        form = TemaForm(request.POST, instance=tema)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tema atualizado com sucesso!')
            return redirect('tema_index')
        else:
            messages.warning(request, 'Um ou mais campos foram preenchidos incorretamente!')
            return render(request, 'temas/editar.html', {'form': form, 'tema': tema})
    else:
        return render(request, 'temas/editar.html', {'form': form, 'tema': tema})
