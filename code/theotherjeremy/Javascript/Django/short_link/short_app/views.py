from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random

from .models import Shortness
# Create your views here.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# step 1:
# def index(request):
#     return HttpResponse('something is indexing')

# def rando(request):
#     return HttpResponse('something random')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# Step 2:
# Inside your view, you can use the render shortcut to render a
# template. The first parameter is the request, the second
# parameter is the name of the template, and the third is a
# dictionary containing the values you'd like to render in the
# template.


# def index(request):
#     return HttpResponse('something is supposed to go here')


def index(request):
    all_Shortnesses = Shortness.objects.all()
    context = {'all_Shortnesses': all_Shortnesses}
    return render(request, 'short_app/index.html', context)


# this is a url.
def shorten_it(request):
    # THESE are query sets. what happens to object when it gets passed in from request?
    # define it, then manipulate it
    # blue "long_url" is from created class in models,
    # other long_url is from 'name' in html

    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rando = ''
    for i in range(6):
        rando += (random.choice(alpha))
    long_url = request.POST['long_url']
    Shortness.objects.create(long_url=long_url, short_url=rando)
    all_Shortnesses = Shortness.objects.all()
    # left is what will be referenced in template, right side = defined above
    context = {'all_Shortnesses': all_Shortnesses}
    # use responseRedirect for when something is happening on same page
    # reverse ('name of app in urls':what page to load (from urls))
    return HttpResponseRedirect(reverse('short_app:index'))

# how we reference "which object?" have to put item.id in html, pass id in as parameter,
# int:id in urls, # then id=id here.


def redirect(request, id):
    short_url = Shortness.objects.get(id=id)
    return HttpResponseRedirect(short_url.long_url)
