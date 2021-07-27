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
    total_clicks = u.clicks
    if ClickData.objects.filter(related_url=url_id).exists():
        u_click_data = ClickData.objects.filter(related_url=url_id).order_by('click_date')[:5]
    else:
        u_click_data = []
    context = {
        'long_url': u.long_url,
        'short_code': u.short_code,
        'short_url': u.short_url,
        'click_data': u_click_data,
        'url_name': u.url_name,
        'clicks': total_clicks,
    }
    return render(request, 'url_shortener/edit_url.html', context)

def delete_url(request, url):
    pass

def search_url(request, url):
    pass

def url_redirect(request, shortcode):
    if UrlShortener.objects.filter(short_code=shortcode).exists():
        u = UrlShortener.objects.filter(short_code=shortcode).get()
        cd = ClickData(related_url=u, ip_addr=request.META['REMOTE_ADDR'], host=request.META['REMOTE_HOST'])
        u.clicks += 1
        u.save()
        cd.save()
        return HttpResponseRedirect(u.long_url)
    else:
        return error(request)

def error(request):
    return render(request, 'url_shortener/error.html')

