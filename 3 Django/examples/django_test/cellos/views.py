from random import choice
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Cello

def cellos(request):
    cellos = Cello.objects.all().order_by('-id')

    if request.method == 'POST':
        Cello.objects.create(
            name=request.POST['name'],
            manufacturer=request.POST['manufacturer'],
            price=request.POST['price'],
            string_count=request.POST['string_count'],
        )

    return render(request, 'cellos/list.html', {'cellos': cellos})

def detail(request, id):
    cello = get_object_or_404(Cello, id=id)

    return render(request, 'cellos/detail.html', {'object': cello})

def random(request):
    cello = choice(Cello.objects.all())

    return JsonResponse({
        'name': cello.name,
        'manufacturer': cello.manufacturer,
        'price': cello.price,
        'string_count': cello.string_count
    })
