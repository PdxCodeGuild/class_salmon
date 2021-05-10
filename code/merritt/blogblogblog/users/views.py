from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from posts.models import Post

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class PostList(generic.ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.filter(author__username__exact=self.kwargs['username']).order_by('-created')

class UserListView(generic.ListView):
    model = User
    template_name = 'user_list.html'