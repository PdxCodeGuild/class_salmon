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
    # Check if the url is already in the Database
    # if yes, check if the code exists
    if Links.objects.filter(url=url).exists():

        return HttpResponse("I'm a duplicate URL!")

    # Check if the code is in the database
    elif Links.objects.filter(code=code).exists():

        return HttpResponseRedirect(url)

    # Create new objects and save
    else:

        return Links.objects.create(url = url, code = code)

    return HttpResponseRedirect(reverse("app_shortURL:index"))

def RedirectURL(request):
    # refer to polls urls example
    # get from the input text URL
    # search for link associated with it
    # return original url
    # # path('<str:question_id>/vote/', views.vote, name='vote'),
    return HttpResponseRedirect("https://www.duckduckgo.com")

def URLEncryption(request):
    # Gather the original URL from the input
    # Set params for the short URL
    # Create the short URL
    url = request.POST['encrypt']
    size = 8
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    code = ''.join(random.choice(chars) for _ in range(size))
    url_string = f"https://www.shor.ty/{code}"
    print(url_string)
