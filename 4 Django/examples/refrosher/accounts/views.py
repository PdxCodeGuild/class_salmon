from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required


def sign_up(request):
    if request.method == 'POST':
        # Store the data from the POST request
        form = UserCreationForm(request.POST)

        # If the form is valid (eg. user's username is unique)
        if form.is_valid():
            # Save the user into the database
            user = form.save()

            # Login the newly created user
            # user = authenticate(
            #     request,
            #     form.cleaned_data['username'],
            #     form.cleaned_data['password1']
            # )
            login(request, user)

            return redirect('/')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/sign_up.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def is_staff_test(user):
    return user.is_staff

@user_passes_test(is_staff_test)
def admin_profile(request):
    pass

@permission_required('thread.delete')
def delete_thread(request):
    pass