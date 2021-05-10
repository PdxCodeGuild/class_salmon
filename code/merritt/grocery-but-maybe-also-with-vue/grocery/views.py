from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from django.core import serializers
import json

from .models import GroceryItem
from .forms import AddForm

def index(request):
    incomplete_items = serializers.serialize('json', GroceryItem.objects.filter(is_completed=False).order_by('-date_created'))
    complete_items = serializers.serialize('json', GroceryItem.objects.filter(is_completed=True).order_by('-date_completed'))
    form = AddForm()
    try:
        error = request.GET['error']
    except:
        error = None
    context = {
        'incomplete_items': incomplete_items,
        'complete_items': complete_items,
        'form': form,
        'error': error,
        }
    return render(request, 'grocery/index.html', context)

def add_item(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            GroceryItem.objects.create(name=form.cleaned_data['name'], date_created=timezone.now())
            return HttpResponseRedirect(reverse('grocery:index'))
        else:
            return HttpResponseRedirect(f'{reverse("grocery:index")}?error=Please enter a name for your new todo')
        
        # if request.POST['name']:
        #     GroceryItem.objects.create(name=request.POST['name'], date_created=timezone.now())
        #     return HttpResponseRedirect(reverse('grocery:index'))
        # else:
        #     return HttpResponseRedirect(f'{reverse("grocery:index")}?error=Please enter a name for your new todo')
    else:
        raise Http404()

def mark_complete(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, pk=pk)
        item.is_completed = True
        item.date_completed = timezone.now()
        item.save()
        return HttpResponseRedirect(reverse('grocery:index'))
    else:
        raise Http404()

def delete(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(GroceryItem, pk=pk)
        item.delete()
        return HttpResponseRedirect(reverse('grocery:index'))
    else:
        raise Http404()