from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import GroceryItem

def index(request):
    print("action >", "index")
    print("url >", request.path)
    print("form >", request.POST)
    completed_items = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
    }
    return render(request, 'grocery/index.html', context)

def new(request):
    print("action >", "new")
    print("url >", request.path)
    print("form >", request.POST)
    description = request.POST['description']
    GroceryItem.objects.create(description=description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    print("action >", "complete")
    print("url >", request.path)
    print("form >", request.POST)
    item = get_object_or_404(GroceryItem, pk=pk)
    item.completed = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    print("action >", "delete")
    print("url >", request.path)
    print("form >", request.POST)
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))