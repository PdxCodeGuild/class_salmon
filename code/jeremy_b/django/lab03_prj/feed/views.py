from django.shortcuts import render
from posts.models import Posts
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    chirps = Posts.objects.all().order_by('-created')
    paginator = Paginator(chirps, 25)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'feed/index.html', context)

