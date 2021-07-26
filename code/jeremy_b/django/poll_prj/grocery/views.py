from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import List, ListItem


def index(request):
    active_list = List.objects.filter(is_active=True)
    inactive_list = List.objects.filter(is_active=False)
    active_list_len = len(active_list)
    inactive_list_len = len(inactive_list)
    return render(request, 'grocery/index.html', {'active_lists': active_list, 'list_len': active_list_len, 'inactive_lists': inactive_list, 'inactive_list_len': inactive_list_len})

def list_detail(request, list_id):
    list_items = ListItem.objects.filter(list_id=list_id)
    item_list_len = len(list_items)
    list_name = List.objects.filter(pk=list_id).get().list_name
    context = {
        'list_items': list_items,
        'item_list_len': item_list_len,
        'list_id': list_id,
        'list_name': list_name,
    }
    return render(request, 'grocery/list_detail.html', context)


def add_list(request):
    if request.POST:
        new_list_name = request.POST
        new_list = List(list_name=new_list_name['list_name'])
        new_list.save()
        return index(request)
    else:
        return render(request, 'grocery/add_list.html')


def add_list_item(request, pk):
    if request.POST:
        list_id = List.objects.filter(pk=pk).get().id
        new_item_name = request.POST
        new_item = ListItem(list_item_text=new_item_name['list_item_name'], list_id=list_id)
        new_item.save()
        return list_detail(request, pk)
    else:
        list_name = List.objects.filter(pk=pk).get().list_name
        return render(request, 'grocery/add_list_item.html', {'list_id': pk, 'list_name': list_name})

def edit_list(request, list_id):
    q = List.objects.filter(pk=list_id).get()
    if request.POST:
        print(request.POST['is_active'])
        if request.POST['is_active'] == 'on':
            q.is_active = True
        else:
            q.is_active = False
        q.list_name = request.POST['list_name']
        q.save()
        return list_detail(request, list_id)
    else:
        context = {
            'list_id': q.pk,
            'list_name': q.list_name,
            'is_active': q.is_active
        }
        return render(request, 'grocery/edit_list.html', context)

def delete_list(request, list_id):
    q = List.objects.get(pk=list_id)
    q.delete()
    return index(request)

def list_disable(request, list_id):
    q = List.objects.get(pk=list_id)
    q.is_active = 0
    q.save()
    return index(request)

def list_enable(request, list_id):
    q = List.objects.get(pk=list_id)
    q.is_active = 1
    q.save()
    return index(request)

def delete_list_item(request, item_id):
    i = ListItem.objects.get(pk=item_id)
    i.delete()
    return list_detail(request, i.list_id)

def item_complete(request, item_id):
    i = ListItem.objects.get(pk=item_id)
    i.is_complete = 1
    i.save()
    return list_detail(request, i.list_id)

def request_complete(request):
    return render(request, 'grocery/request_complete.html')


