from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

# The manual way
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate, logout
# def sign_in(request):
#     errors = []

#     if request.method == 'POST':
#         user = authenticate(
#             request,
#             username=request.POST['username'],
#             password=request.POST['password'],
#         )
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             errors.append("Invalid login information!")

#     return render(request, 'accounts/login.html', {'errors': errors})

# def sign_out(request):
#     logout(request)
#     return redirect('/')

# def register(request):
#     errors = []

#     if request.method == 'POST':
#         if request.POST['password'] == request.POST['password_confirm']:
#             user = User.objects.create_user(
#                 username=request.POST['username'],
#                 email=request.POST['email'],
#                 password=request.POST['password'],
#             )
            
#             login(request, user)
#             return redirect('/')
#         else:
#             errors.append("Mismatching passwords!")
    
#     return render(request, 'accounts/register.html', {'errors': errors})

