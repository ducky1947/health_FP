from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def item_list(request):
    items = Item.objects.all()
    return render(request, 'core/item_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'core/item_detail.html', {'item': item})

def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'core/item_edit.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'core/item_edit.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'core/item_delete.html', {'item': item})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('item_list')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})