from django.urls import path
from . import views 

urlpatterns = [
    path("login/", views.login, name = "login"),
    path("signup/", views.signup, name = "signup"),
    path("token/", views.test_token, name = "test_token")
]