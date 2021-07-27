from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem
# Create your views here.

def index(request):
    grocery_item_list = GroceryItem.objects.order_by('-created_date')
    context = {
        'grocery_item_list' : grocery_item_list
    }
    return render(request, 'grocery_list/index.html', context)

def detail(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    return render(request, 'grocery_list/detail.html', {'grocery_item': grocery_item})

def updates(request,grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    
    return HttpResponseRedirect(reverse('grocery_list:index',args=[grocery_item.id]))
def deleteItem(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    
    return render(request, 'grocery_list/index.html', context)