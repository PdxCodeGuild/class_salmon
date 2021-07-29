from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Shortener
import random

def index(request):
    # return HttpResponse('it worked!')
    # code = Shortener.objects.all()
    # url = request.POST['url']
    url = request.POST['url']
    code = []
    for i in range(6): 
        code.append(random.choice('abcdefghijklmnopqrstuvwxyz1234567890'))
    code = ''.join(code)
    Shortener.objects.create(url=url, code=code)
    print("URL: " + url)
    context = {
        'url': url,
        'code': code,
    }
    return render(request, 'url_short/index.html', context)

def redirect(request):
    code = get_object_or_404(Shortener, pk=pk)
    return HttpResponseRedirect(code)