from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from posts.models import Posts

import feed.views

# Create your views here.
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(feed.views.index)
    else:
        form = UserCreationForm()

    return render(request, 'users/signup.html', {'form': form})

def profile(request, username):
    user = User.objects.filter(username=username).values('id', 'last_login', 'date_joined')
    author = {'id':user[0]['id'], 'date_joined':user[0]['date_joined'], 'last_login':user[0]['date_joined'], 'username':username}

    user_chirps = Posts.objects.filter(author=author['id']).values()
    print(user_chirps)
    context = {
        'chirps': user_chirps,
        'author': author
    }
    return render(request, 'accounts/profile.html', context)
