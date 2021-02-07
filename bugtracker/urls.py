from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("buglistpage", views.buglistpage, name="buglistpage"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bugdetails", views.bugdetails, name="deteails"),

    # API Routes
    path("buglistmessages", views.buglistmessages, name="buglistmessages")
]