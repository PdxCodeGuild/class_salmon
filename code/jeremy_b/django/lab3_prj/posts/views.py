
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

class PostView(ListView):
    model = Post
    template_name = 'index.html'
    title = 'Quackr'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    title = 'Quack Detail'


class CreatePost(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['body', 'image']
    title = 'New Quack'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['body', 'image']
    title = 'Edit Quack'

    def test(self):
        post = self.get_object()
        return self.request.user == post.post_author

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts:index')
    title = 'Delete Quack'

    def test(self):
        post = self.get_object()
        return self.request.user == post.post_author