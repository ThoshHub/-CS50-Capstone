from django.urls import path
from . import views

urlpatterns = [
    # All paths are prefixed with /bugtraceker, so login -> bugtracker/login, for example
    path("", views.index, name="index"),
    path("buglistpage", views.buglistpage, name="buglistpage"), # returns page with user org's bugs
    path("userbuglistpage", views.userbuglistpage, name="userbuglistpage"), # returns page with ONLY user's bugs
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bugdetailspage/<int:bug_id>", views.bugdetailspage, name="bugdetailspage"), # returns page with details of that id
	path("bugdetailspage/<int:bug_id>/edit", views.bugdetailedit, name="bugdetailedit"), # returns form to edit bug
    path("createbug", views.createbug, name="createbug"), # create a new bug

    # API Routes
    path("buglistmessages", views.buglistmessages, name="buglistmessages"), # gives a list of all messages that belong to user's organization
    path("userbuglistmessage", views.userbuglistmessages, name="userbuglistmessages"),
    path("bugdetailcontent/<int:bug_id>", views.bugdetailcontent, name="bugdetailcontent"), # returns JSON with details of that id
    path("usermessagecount", views.usermessagecount, name="usermessagecount"), # returns json with count of total bugs assigned to org, and total bugs assigned to user
    path("completebug/<int:bug_id>", views.completebug, name="completebug") # marks bug with id passed in as complete (sets 'active' = false)
]