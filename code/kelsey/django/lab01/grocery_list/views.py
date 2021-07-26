from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    groceryitems = GroceryItem.objects.all()
    context = {
        'groceryitems': groceryitems
    }
    return render(request, 'grocery_list/index.html', context)

def addItem(request):
    new_item = request.POST["add"]
    GroceryItem.objects.create(text=new_item)
    return HttpResponseRedirect(reverse("grocery_list:grocery_list"))

# def completeItem(request):
#     return HttpResponse('<h1>Complete Items</h1>')

def deleteItem(request, id):
    del_item = get_object_or_404(GroceryItem, id=id)
    del_item.delete()
    return HttpResponseRedirect(reverse("grocery_list:grocery_list"))