from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import random, string
from .models import Links

def index(request):
    link_list = Links.objects.all()
    context = {
        "link_list": link_list,
    }
    return render(request, "app_shortURL/index.html", context)

def InputURL(request):
    # Gather the original URL from the input
    original_url = request.POST['input_URL']

    # Set params for the short URL
    size = 8
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    # Create the short URL
    short_url = ''.join(random.choice(chars) for _ in range(size))

    # Check if the original_URL is already in the Database
    # if yes, check if the short_url exists
    #
    if Links.objects.filter(original_url=original_url).exists():

        return HttpResponseRedirect("http://www.duckduckgo.com")
    # Check if the short_url is in the database
    elif Links.objects.filter(short_url=short_url).exists():
        print("line 32 url not found")
        return HttpResponseRedirect(original_url)
    # Create new objects and save
    else:
        return Links.objects.create(original_url = original_url, short_url = short_url)




    return HttpResponseRedirect(reverse("app_shortURL:index"))

def RedirectURL(request):
    # refer to polls urls example
    # path('<str:question_id>/vote/', views.vote, name='vote'),
    return HttpResponseRedirect("Hi")
