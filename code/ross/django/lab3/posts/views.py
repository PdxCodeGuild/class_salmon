from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from .models import Post

# renders the 'feed'
class Home(ListView):
    model = Post
    template_name = 'home.html'

    def home(request):
        chirp = Post.objects.all()
        context = {'chirp': chirp}
        return render(request, 'posts/home.html', context)

class CreateChirp(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_chirp.html'
    fields = ['contents']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# displays Chirp feed
# class ChirpFeed():
#     print(request.POST)
#     contents = request.POST
#     user = User
#     Post.objects.create(contents=contents, author=User)
#     return HttpResponseRedirect(reverse('posts:index'))