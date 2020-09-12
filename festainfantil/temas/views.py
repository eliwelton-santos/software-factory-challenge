from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Tema
from itens.models import Item
from .forms import TemaForm


def redirecionar(request):
    return redirect('tema_index')


def index(request):
    temas = Tema.objects.all().order_by('-created_at')
    return render(request, 'temas/index.html', {'temas': temas})


def detalhe(request, id):
    tema = get_object_or_404(Tema, pk=id)
    itens = Item.objects.filter(tema=id)
    return render(request, 'temas/detalhe.html', {'tema': tema, 'itens': itens})


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


def deletar(request, id):
    tema = get_object_or_404(Tema, pk=id)
    tema.delete()
    messages.success(request, 'Tema deletado com sucesso!')
    return redirect('tema_index')
