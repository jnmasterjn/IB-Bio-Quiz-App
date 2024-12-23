from django.urls import path
from . import views #import views from current app

# define URL patterns for the app
urlpatterns = [
    path("login/", views.login, name = "login"),
    path("signup/", views.signup, name = "signup"),
    path("token/", views.test_token, name = "test_token"),
    path("quiz/", views.get_quiz, name = "quiz"),
    path("score/", views.update_score, name = "score"),
    path("leaderboard/", views.leaderboard, name = "leaderboard")
]