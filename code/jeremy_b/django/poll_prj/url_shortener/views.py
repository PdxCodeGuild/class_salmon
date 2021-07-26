from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from .models import UrlShortener, ClickData
from requests import request as rq

# Create your views here.
def index(request):
    # Get a list of all active URL's
    active_url_list = UrlShortener.objects.filter(is_active=True)
    inactive_url_list = UrlShortener.objects.filter(is_active=False)
    active_list_len = len(active_url_list)
    inactive_list_len = len(inactive_url_list)

    context = {
        'active_urls': active_url_list,
        'active_list_len': active_list_len,
        'inactive_urls': inactive_url_list,
        'inactive_list_len': inactive_list_len
    }

    return render(request, 'url_shortener/index.html', context)

def add_new_url(request):
    if request.POST:
        url_data = request.POST
        short_code = rq('get', 'http://random-word-api.herokuapp.com/word?number=1')
        short_code = short_code.text.strip('[""]')
        short_url = 'http://127.0.0.1:8484/url_shortener/to/' + short_code
        u = UrlShortener(url_name=url_data['url_name'], long_url=url_data['long_url'], short_code=short_code, short_url=short_url)
        u.save()
        return index(request)
    else:
        return render(request, 'url_shortener/add_url.html')

def edit_url(request, url_id):
    u = UrlShortener.objects.filter(pk=url_id).get()
    u_click_data = ClickData.objects.filter(pk=url_id)
    if request.POST:
        pass
    else:
        context = {
            'long_url': u.long_url,
            'shortcode': u.short_code,
            'short_url': u.short_url,
            'click_data': u_click_data

        }

def delete_url(request, url):
    pass

def search_url(request, url):
    pass

def url_redirect(request, url):
    pass
