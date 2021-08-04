from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.urls import reverse
# Create your views here.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# step 1:
# def index(request):
#     return HttpResponse('something is indexing')

# def rando(request):
#     return HttpResponse('something random')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# Step 2:
# Inside your view, you can use the render shortcut to render a
# template. The first parameter is the request, the second
# parameter is the name of the template, and the third is a
# dictionary containing the values you'd like to render in the
# template.

# this is a url


def index(request):
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'chirp_app/index.html', context)


def user_login(request):
    current_auth = request.user
    context = {'current_auth': current_auth}
    return render(request, 'chirp_app/user_profile.html', context)


def add_item(request):
    new_item = request.POST.get('new_item')
    author = request.user
    Post.objects.create(item_text=new_item, author=author)
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return HttpResponseRedirect(reverse('users:user_profile'))


def delete_item(request, id):
    delete_item = Post.objects.get(id=id)
    delete_item.delete()
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'chirp_app/index.html', context)
