from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from pokemon.models import Pokemon
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserAppProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
def catch(request):
    username = request.POST['username']
    pokemon = request.POST['pokemon']
    caught = get_object_or_404(Pokemon, pk=pokemon)
    caught.caught_by_user.add(request.user)
    caught.save()
    print(caught)
    return HttpResponseRedirect('')