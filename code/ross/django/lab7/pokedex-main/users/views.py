from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from pokemon.models import Pokemon
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect


from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def catch(request):
    print(request.POST)
    # print("pk: " + pk)
    # print("username: " + username)
    username = request.POST['username']
    pokemon = request.POST['pokemon']
    print('pokemon: ' + pokemon)
    print('user: ' + username)
    caught = get_object_or_404(Pokemon, pk=pokemon)
    caught.caught_by_users.add(request.user)
    caught.save()
    print(caught)
    return HttpResponseRedirect('/')
