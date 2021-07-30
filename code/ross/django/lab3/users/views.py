from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView
# from .models import User

def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('posts:home'))
    return render(request, 'newacct.html', {'form': form})

def login_view(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('posts:home'))
    else:
        context = {'user': user}
        return HttpResponse('Sorry, please enter a valid username/password or sign up.')
        # return render(request, 'registration/invalid.html', context)
    context = {'user': user}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('logout/')

# def user_profile(request, username):
#     chirps = Post.objects.all()
#     user_profile = User.objects.all() # .filter(username)
#     context = {
#         'chirp': chirps,
#         'user_profile': user_profile
#         }
#     return render(request, 'user_profile.html', context)

class UserProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])