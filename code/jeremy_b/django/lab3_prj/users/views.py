from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
class Signup(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    title = 'Signup'

class UserProfile(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'
    title = 'Profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

