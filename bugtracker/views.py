from collections import UserDict
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models import Value, IntegerField
from django.http import HttpResponse, HttpResponseRedirect
from django.http import request
from django.shortcuts import render
from django.urls import reverse
# from .forms import messageForm
# from .models import User, message
from django.http import JsonResponse
from django.core import serializers
import json
from datetime import date, datetime
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, "bugtracker/index.html")

def login_view(request):
	if request.method == "POST":

		# Attempt to sign user in
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)

		# Check if authentication successful
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "bugtracker/login.html", {
				"message": "Invalid username and/or password."
			})
	else:
		return render(request, "bugtracker/login.html")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))


def register(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]

		# Ensure password matches confirmation
		password = request.POST["password"]
		confirmation = request.POST["confirmation"]
		if password != confirmation:
			return render(request, "bugtracker/register.html", {
				"message": "Passwords must match."
			})

		# Attempt to create new user
		try:
			user = User.objects.create_user(username, email, password)
			user.save()
		except IntegrityError:
			return render(request, "bugtracker/register.html", {
				"message": "Username already taken."
			})
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "bugtracker/register.html")

# returns an html page that contains list of bugs retrieved from the database
def buglistpage(request):
	# Need to grab list of bugs that 
	return render(request, "bugtracker/buglistpage.html")

# returns a list of bugs retrieved from database in JSON form
def buglistmessages(request):
	data = "{\"name\":\"John\", \"age\":31, \"city\":\"New Yorkk\"}" # Dummy Data for Debugging
	return JsonResponse(data, safe=False)

# returns a list of bugs in list format
def querybugs():
	# TODO need to pass in id of user requesting data
	# From there get the org that the user works for
	# Then get all bugs under that org
	# Put the ids of the bugs into a list 
	# Return this list

	return "test"

def createbug(request):
	return render(request, "bugtracker/error.html")