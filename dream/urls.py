from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("new_dream", views.new_dream, name="new_dream"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("register", views.register, name="register"),
]