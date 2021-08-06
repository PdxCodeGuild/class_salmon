import datetime
import secrets
import string
from django.utils import timezone

from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from .models import SubmittedUrl
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    url_list = SubmittedUrl.objects.all()#.filter(create_date__lte=timezone.now()).order_by('-id')[0]
    # print(url_list)
    latest_url = SubmittedUrl.objects.all().filter(create_date__lte=timezone.now()).order_by('-id')[0]
    context = {
        'url_list': url_list,
        'latest_url': latest_url
               }
    return render(request, 'url_shortener_app/index.html', context)#attributes are: 1. the request 2. the template 3. the dictionary

def template2(request):#this may not be necessary to have as a function, unless the user types url_shortener_app/template2.html into browser
    url_list = SubmittedUrl.objects.all()#.filter(create_date__lte=timezone.now()).order_by('-id')[0]
    # print(url_list)
    latest_url = SubmittedUrl.objects.all().filter(create_date__lte=timezone.now()).order_by('-id')[0]
    context = {
        'url_list': url_list,
        'latest_url': latest_url
               }
    return render(request, 'url_shortener_app/template2.html', context)#attributes are: 1. the request 2. the template 3. the dictionary

def submit_url(request):
    new_url = request.POST['new_url']
    # print(new_url)
    alphabet = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(alphabet) for i in range(8)) #8 character code
    # print(code)#working
    latest_url = SubmittedUrl.objects.all().filter(create_date__lte=timezone.now()).order_by('-id')[0]
    SubmittedUrl.objects.create(url_description=new_url, code_for_url=code)
    context = {
        'latest_url': latest_url
               }
    return render(request, 'url_shortener_app/template2.html', context)
    # return HttpResponseRedirect(reverse('url_shortener_app:template2'))

def url_by_code(request, from_user):
    # print('request path is ' + request.path)
    # print('request body is ' + request.body)
    # print('request path_info is ' + request.path_info)
    code = get_object_or_404(SubmittedUrl, code_for_url=from_user)
    # print(from_user + ' line 38') #only the short url, 
    return HttpResponseRedirect(code.url_description)
