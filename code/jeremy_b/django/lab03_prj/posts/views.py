from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Posts

class NewPost(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'posts/add_post.html'
    fields = ['body']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
