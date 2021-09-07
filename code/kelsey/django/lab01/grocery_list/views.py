from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    completed_items = GroceryItem.objects.filter(completed=True).order_by('-completed_date')
    incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created')
    context = {
        'completed_items': completed_items,
        'incomplete_items': incomplete_items
    }
    return render(request, 'grocery_list/index.html', context)

def addItem(request):
    new_item = request.POST['add']
    GroceryItem.objects.create(text=new_item)
    return HttpResponseRedirect(reverse("grocery_list:grocery_list"))

def completeItem(request, id):
    item = get_object_or_404(GroceryItem, id=id)
    item.completed = False if item.completed else True
    item.completed_date = timezone.now() if item.completed else None
    item.save()
    return HttpResponseRedirect(reverse("grocery_list:grocery_list"))

def deleteItem(request, id):
    del_item = get_object_or_404(GroceryItem, id=id)
    del_item.delete()
    return HttpResponseRedirect(reverse("grocery_list:grocery_list"))