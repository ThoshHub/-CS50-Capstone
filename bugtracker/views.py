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

def buglist(request):
	# Need to grab list of bugs that 
	return render(request, "bugtracker/buglist.html")

def createbug(request):
	return render(request, "bugtracker/error.html")