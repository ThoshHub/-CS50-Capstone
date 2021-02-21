from django.urls import path
from . import views

urlpatterns = [
    # All paths are prefixed with /bugtraceker, so login -> bugtracker/login, for example
    path("", views.index, name="index"),
    path("buglistpage", views.buglistpage, name="buglistpage"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bugdetailspage/<int:bug_id>", views.bugdetailspage, name="bugdetailspage"), # returns page with details of that id
	path("bugdetailspage/<int:bug_id>/edit", views.bugdetailedit, name="bugdetailedit"), # returns form to edit bug
    path("createbug", views.createbug, name="createbug"), # create a new bug

    # API Routes
    path("buglistmessages", views.buglistmessages, name="buglistmessages"), # gives a list of all messages that belong to user's organization
    path("bugdetailcontent/<int:bug_id>", views.bugdetailcontent, name="bugdetailcontent"), # returns JSON with details of that id
    
]