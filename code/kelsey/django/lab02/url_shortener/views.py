from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Shortener
import random, string

def index(request):
    shorteners = Shortener.objects.all()
    context = {
        'shorteners': shorteners
    }
    return render(request, 'url_shortener/index.html', context)
   
def shorty(request):
    long_url = request.POST['long_url']
    short_url = ''
    for i in range(6):
        short_url += random.choice(string.printable)
    Shortener.objects.create(long_url=long_url, short_url=short_url)
    return HttpResponseRedirect(reverse('url_shortener:index'))
