# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from .models import Shortener
# import random, string
# from string import ascii_letters, digits

# def redirect(request):
#     shorteners = Shortener.objects.all()
#     context = {
#         'shorteners': shorteners
#     }
#     return render(request, 'url_short/index.html', context)
   
# def index(request):
#     url = request.POST['url']
#     available_chars= ascii_letters + digits
#     code = ''
#     for i in range(10):
#         code += random.choice(available_chars)
#     Shortener.objects.create(url=url, code=code)
#     return HttpResponseRedirect(reverse('url_short:index'))



from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Shortener
import random
from string import ascii_letters, digits

def index(request):
    available_chars= ascii_letters + digits
    code = []
    for i in range(10): 
        code.append(random.choice(available_chars))
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
    return HttpResponseRedirect(redirect_url)