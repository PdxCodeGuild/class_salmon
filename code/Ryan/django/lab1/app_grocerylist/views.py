from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Item

def index(request):
    item_list = Item.objects.all()
    context = {
        "item_list": item_list
    }
    return render(request, "grocerylist/index.html", context)

# Create Item
def CreateItem(request):
    # Text Description
    item_text = request.POST["add_item"]
    # Created date
    created_date = timezone.now()
    Item.objects.create(item_text = item_text, created_date = created_date)
    return HttpResponseRedirect(reverse('app_grocerylist:index'))

# Delete Item
def DeleteItem(request, id):
    # ID
    item_id = get_object_or_404(Item, pk=id)
    item_id.delete()
    return HttpResponseRedirect(reverse('app_grocerylist:index'))

# Update Item
def UpdateItemStatus(request, id):
    # ID
    item_id = get_object_or_404(Item, pk=id)
    # Completed Date
    completed_date = timezone.now()

    # Change Status
    if item_id.completed == False:
        item_id.completed = True
        item_id.completed_date = completed_date
        item_id.save()
    else:
        item_id.completed = False
        item_id.save()
    return HttpResponseRedirect(reverse('app_grocerylist:index'))
