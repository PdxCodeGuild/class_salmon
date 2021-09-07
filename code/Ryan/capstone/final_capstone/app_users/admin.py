from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "first_name", "last_name", "wins", "losses", "user_image" ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("wins","losses")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
