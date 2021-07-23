from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from .models import GroceryItem
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    grocery_list = GroceryItem.objects.all() #.filter(completed_date__lte=timezone.now()).order_by('-completed_date')[:5] #descending completed_date
    print(grocery_list)
    context = {
        'grocery_list': grocery_list       }
    return render(request, 'groceries/index.html', context)#attributes are: 1. the request 2. the template 3. the dictionary

def add_grocery(request):
    new_item = request.POST['new_item']
    print(new_item)
    GroceryItem.objects.create(item_description=new_item)
    return HttpResponseRedirect(reverse('groceries:index'))

def delete_grocery(request, id):
    delete_item = get_object_or_404(GroceryItem, id=id)
    print(delete_item)
    delete_item.delete()
    return HttpResponseRedirect(reverse('groceries:index'))