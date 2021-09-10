from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created! You may now login.")
            return redirect("app_posts:posts-login")
    else:
        form = UserRegisterForm()
    return render(request, "app_users/register.html", {"form": form})

@login_required
def profile(request):
    return render(request, "app_users/profile.html")