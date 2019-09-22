from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.aboutme, name="aboutme"),
    path("register", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),
    path("projects", views.projects, name="projects"),
    path("<single_slug>", views.single_slug, name="single_slug"),
]
