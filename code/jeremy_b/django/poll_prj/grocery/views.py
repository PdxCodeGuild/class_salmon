from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import List, ListItem


def index(request):
    active_lists = List.objects.filter(is_active=True)
    list_len = len(active_lists)
    return render(request, 'grocery/index.html', {'active_lists': active_lists, 'list_len': list_len})

def list_detail(request, list_id):
    list_items = ListItem.objects.filter(list_id=list_id).filter(is_complete=False)
    item_list_len = len(list_items)
    return render(request, 'grocery/list_detail.html', {'list_items': list_items, 'item_list_len': item_list_len })


def add_list(request):
    if request.POST:
        new_list_name = request.POST
        print(new_list_name)
        print(new_list_name['list_name'])
        new_list = List(list_name=new_list_name['list_name'])
        new_list.save()
        return HttpResponseRedirect(reverse('grocery:request_complete'))
    else:
        return render(request, 'grocery/add_list.html')


def add_list_item(request):
    pass

def edit_list(request):
    return render(request, 'grocery/edit_list.html')

def edit_list_item(request):
    pass

def delete_list(request):
    pass

def delete_list_item(request):
    pass

def request_complete(request):
    return render(request, 'grocery/request_complete.html')


