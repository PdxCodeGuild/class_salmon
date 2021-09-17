from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "app_posts/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = "app_posts/home.html" # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date_posted"]

class PostDetailView(DetailView):
    model = Post
    template_name = "app_posts/post_detail.html" # <app>/<model>_<viewtype>.html

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "app_posts/post_form.html" # <app>/<model>_<viewtype>.html
    fields = [
        'title', 
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "app_posts/post_confirm_delete.html" # <app>/<model>_<viewtype>.html
    fields = ['title', 'content']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # success_url = '/'
    template_name = "app_posts/post_confirm_delete.html" # <app>/<model>_<viewtype>.html
    success_url = reverse_lazy('posts:home')

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    return render(request, "app_posts/about.html", {"title": "About"})

