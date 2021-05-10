from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from ipware import get_client_ip

from .models import URL, Click

def home(request):
    if request.method == 'POST':
        url = URL()
        url.long_url = request.POST['long_url']
        url.generate_code()
        url.save()

        return render(request, 'shortener/home.html', {'url': url})
    
    return render(request, 'shortener/home.html')

def redirect(request, code):
    url = get_object_or_404(URL, code=code)

    click = Click()
    click.http_referer = request.META['HTTP_REFERER']
    click.ip_address = get_client_ip(request)
    click.url = url
    click.save()
        
    return HttpResponseRedirect(url.long_url)