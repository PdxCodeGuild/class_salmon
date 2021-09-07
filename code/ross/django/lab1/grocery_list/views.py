from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import GroceryItem
from .forms import ItemForm

def index(request):
    items = GroceryItem.objects.all
    # completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    # incomplete_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    # context = {
    #     'completed_items': completed_items,
    #     'incomplete_items': incomplete_items
    # }
    context = {'items': items}
    return render(request, 'grocery_list/index.html', context)
    
def new(request):
    print(request.method)
    description = request.POST['description']
    item = GroceryItem(description=description, created_date=timezone.now(), completed=False)
    item.save()
    return HttpResponseRedirect('/')

def complete(request, item_id):
    print(item_id)
    print(request.method)
    print(request.path)
    item = GroceryItem.objects.get(pk=item_id)
    item.completed = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect('/')
    # item = get_object_or_404(GroceryItem, pk=pk)
    # item.completed = True if not item.completed else False
    # item.completed_date = timezone.now() if item.completed == True else none
    # item.save()

def delete(request, item_id):
    print('ID: ' + item_id)
    print(request.path)
    item = GroceryItem.objects.get(pk=item_id)
    item.delete()
    return HttpResponseRedirect('/')
