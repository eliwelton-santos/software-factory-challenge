from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Item
from temas.models import Tema
from .forms import ItemForm


def imagem(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.itemPic:
        return render(request, 'itens/imagem.html', {'item': item})
    else:
        messages.warning(request, 'Esse item não possui imagem cadastrada!')
        return redirect('tema_detalhe', id=item.tema.id)


def adicionar(request, id):
    tema = get_object_or_404(Tema, pk=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.tema = tema
            item.save()
            messages.success(request, 'Item adicionado com sucesso!')
            return redirect('tema_detalhe', id=id)
        else:
            messages.warning(request, 'Um ou mais campos foram preenchidos incorretamente!')
            return render(request, 'itens/adicionar.html', {'form': form, 'tema': tema})
    else:
        form = ItemForm()
        return render(request, 'itens/adicionar.html', {'form': form, 'tema': tema})


def editar(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item atualizado com sucesso!')
            return redirect('tema_detalhe', id=item.tema.id)
        else:
            messages.warning(request, 'Um ou mais campos foram preenchidos incorretamente!')
            return render(request, 'itens/editar.html', {'form': form, 'item': item})
    else:
        return render(request, 'itens/editar.html', {'form': form, 'item': item})


def deletar(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    messages.success(request, 'Item deletado com sucesso!')
    return redirect('tema_detalhe', id=item.tema.id)
