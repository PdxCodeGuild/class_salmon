from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import random, string
from .models import Links

def test(request):
    return render(request, "app_shortURL/base.html")

def home(request):
    link_list = Links.objects.all()
    context = {
        "link_list": link_list,
    }
    return render(request, "app_shortURL/home.html", context)

def RedirectURL(request):
    shortURL = request.POST["short_URL"]
    originalURL = Links.objects.get(code=shortURL)
    return HttpResponseRedirect(str(originalURL))

def URLEncryption(request):
    originalURL = request.POST['input_URL']
    size = 8
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    code = ''.join(random.choice(chars) for _ in range(size))
    url_string = f"https://www.shor.ty/{code}"
    
    link = Links(url = originalURL, code = url_string)
    link.save()
    return home(request)