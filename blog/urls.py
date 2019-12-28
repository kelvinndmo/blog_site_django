"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("", include('bloggs.urls')),
    path("auth/", include('authentication.urls')),
    path("auth/login", auth_views.LoginView.as_view(
        template_name="authentication/login.html"), name='login'),
    path("auth/logout", auth_views.LogoutView.as_view(
        template_name="authentication/logout.html"), name='logout'),
    path("auth/password-reset", auth_views.PasswordResetView.as_view(
         template_name="authentication/password_reset.html"), name='password-reset'),
    path("auth/password-done", auth_views.PasswordResetDoneView.as_view(
        template_name="authentication/password_reset_done.html"), name='password_reset_done'),
    path("auth/password-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="authentication/password_reset_confirm.html"), name='password_reset_confirm'),
    path("auth/password_reset_complete", auth_views.PasswordResetCompleteView.as_view(
        template_name="authentication/password_complete.html"), name='password_reset_complete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
