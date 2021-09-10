from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Grocery
from django.urls import reverse
from django.utils import timezone

def index(request):
    grocery_list = Grocery.objects.all()
    # completed_items = Grocery.objects.filter(completed=True)
    context = {
        'grocery_list': grocery_list,

    }
    print(grocery_list)
    return render(request, 'index.html', context)

def add_item(request):
    new_item = request.POST['newItem']
    Grocery.objects.create(item_text=new_item, date_added=timezone.now(), purchased=False)
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete_item(request, id):
    item = Grocery.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))

# Create your views here.