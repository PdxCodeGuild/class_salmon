from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    completed_items = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
    }
    return render(request, 'grocery/index.html', context)

def new(request):
    description = request.POST['description']
    GroceryItem.objects.create(description=description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.completed = False if item.completed else True
    item.completed_date = timezone.now() if item.completed else None
    item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))