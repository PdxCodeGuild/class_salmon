from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponse

from .models import GroceryItem
# Create your views here.

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# step 1:
# def index(request):
#     return HttpResponse('something is indexing')

# def rando(request):
#     return HttpResponse('something random')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# Step 2:
# Inside your view, you can use the render shortcut to render a
# template. The first parameter is the request, the second
# parameter is the name of the template, and the third is a
# dictionary containing the values you'd like to render in the
# template.


def index(request):
    # populate empty lists below
    incomplete_items = GroceryItem.objects.filter(done_box=False)
    complete_items = GroceryItem.objects.filter(done_box=True)
    context = {'incomplete_items': incomplete_items,
               'complete_items': complete_items}
    return render(request, 'grocery_app/index.html', context)


def add_item(request):
    new_item = request.POST['new_item']
    GroceryItem.objects.create(item_text=new_item)
    incomplete_items = GroceryItem.objects.filter(done_box=False)
    complete_items = GroceryItem.objects.filter(done_box=True)
    context = {'incomplete_items': incomplete_items,
               'complete_items': complete_items}
    return render(request, 'grocery_app/index.html', context)


def delete_item(request, id):
    delete_item = GroceryItem.objects.get(id=id)
    delete_item.delete()
    incomplete_items = GroceryItem.objects.filter(done_box=False)
    complete_items = GroceryItem.objects.filter(done_box=True)
    context = {'incomplete_items': incomplete_items,
               'complete_items': complete_items}
    return render(request, 'grocery_app/index.html', context)


def check_item(request, id):
    # GroceryItem.objects.create(item_text=new_item)
    check_item = GroceryItem.objects.get(id=id)
    check_item.done_box = True
    check_item.save()
    incomplete_items = GroceryItem.objects.filter(done_box=False)
    complete_items = GroceryItem.objects.filter(done_box=True)
    context = {'incomplete_items': incomplete_items,
               'complete_items': complete_items}
    return render(request, 'grocery_app/index.html', context)


# add functions that reroute back to index,
# add item, delete
