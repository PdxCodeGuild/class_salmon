from django.shortcuts import render
from django.utils import timezone
from .models import GroceryItem

def post_list(request):
    items = GroceryItem.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'grocery_list/post_list.html', {'items': items})