from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import URL
import random
import string

def shorten():
    short_url = []
    for i in range(5):
        short_url += random.choice(string.ascii_letters)
    num = str(random.randint(0, 9))
    index = random.randint(0, 4)
    short_url[index] = num
    output = ''
    for i in short_url:
        output += i
    # output = f'{link}'
    return output


# Create your views here.
def index(request):
    url_shortener = URL.objects.all()
    context = {
        'url_shortener': url_shortener
    }
    return render(request, 'index.html', context)

def add_url(request):
    url = request.POST['url']
    link = shorten()
    URL.objects.create(short_url=link, full_url=url, date_created=timezone.now())
    return HttpResponseRedirect(reverse('url_shortener:index'))

def visit_url(request, short_url):
    # url = request.POST['visit-url']
    redirect = get_object_or_404(URL, short_url=short_url)
    print(redirect.full_url)
    return HttpResponseRedirect(f'http://{redirect.full_url}')