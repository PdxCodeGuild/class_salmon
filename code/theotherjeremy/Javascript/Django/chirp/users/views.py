from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:login')


class Login(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('chirp_app:index')


def user_profile(request):
    user = request.user
    context = {"user_profile": user}
    return render(request, "chirp_app/user_profile.html", context)


class UserProfileView(DetailView):
    model = User
    template_name = 'users/user_profile.html'
    # context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
