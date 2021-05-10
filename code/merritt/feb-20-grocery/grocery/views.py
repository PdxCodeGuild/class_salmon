from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    incompleted_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    context = {
        'incompleted_items': incompleted_items,
        'completed_items': completed_items
    }
    return render(request, 'grocery/index.html', context)

def add(request):
    if request.POST['description']:
        GroceryItem.objects.create(created_date=timezone.now(), description=request.POST['description'])
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    if item.completed:
        item.completed = False
        item.completed_date = None
    else:
        item.completed = True
        item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))
