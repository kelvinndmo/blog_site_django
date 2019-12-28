from django.urls import path
from .views import register, profile

urlpatterns = [
    path('register', register, name="register-authentication"),
    path('profile', profile, name="profile-authentication")
]
