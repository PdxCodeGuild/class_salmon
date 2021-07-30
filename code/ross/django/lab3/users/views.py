from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, DetailView
# from .models import User

class SignUpView(CreateView):
    create_account = UserCreationForm
    template_name = 'newacct.html'
    good_login = reverse_lazy('login')

class UserProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'
    
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])