from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Shortener
import random

def index(request):
    # url = ''
    print(request.POST['site'])
    code = []
    for i in range(6): 
        code.append(random.choice('abcdefghijklmnopqrstuvwxyz1234567890'))
    code = ''.join(code)
    site = request.POST['site']
    Shortener.objects.create(url=site, code=code)
    # print("URL: " + url)
    context = {
        'site': site,
        'code': code,
    }
    return render(request, 'url_short/index.html', context)

def redirect(request):
    # code = get_object_or_404(Shortener, pk=pk)
    redirect_code = request.POST['code']
    print(redirect_code)
    redirect_url = Shortener.objects.get(code=redirect_code) # figure out how to get the redirect code from the given code and pass it to the redirect
    # redirect_url = Shortener.red.get(code=redirect_code) # figure out how to get the redirect code from the given code and pass it to the redirect
    print(redirect_url)
    redirect_url = str(redirect_url)
    print('redirect' + str(redirect_url))
    # print(redirect_url.Shortener)
    return HttpResponseRedirect(redirect_url)