from django.contrib import admin
from django.urls import path, include
from app_users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="app_users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="app_users/logout.html"), name="logout"),
    path("", include("app_posts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)