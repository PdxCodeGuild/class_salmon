from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem
from .forms import ItemForm

def index(request):
    # items = GroceryItem.objects.filter(created_date__lte=timezone.now()).order_by('description')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
    }
    return render(request, 'grocery_list/index.html', context)
    
def new(request):
    description = request.POST['description']
    GroceryItem.objects.create(description=description, created_date=timezone.now(), completed=False)
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.completed = True if not item.completed else False
    item.completed_date = timezone.now() if item.completed == True else none
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))
