from collections import UserDict
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models import Value, IntegerField
from django.http import HttpResponse, HttpResponseRedirect
from django.http import request
from django.shortcuts import render
from django.urls import reverse
# from .forms import messageForm
from .models import User, bug, organization
from django.http import JsonResponse
from django.core import serializers
import json
from datetime import date, datetime
from django.utils import timezone
from django.db.models import Q
from .forms import bugCreateForm

# Create your views here.
def index(request):
	if not request.user.is_authenticated: # if the user is not authenticated, take them to the login page
		return render(request, "bugtracker/login.html")
	else: # if the user is logged in, take them to the buglist page
		# return render(request, "bugtracker/index.html")
		return render(request, "bugtracker/buglistpage.html")

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
	id = currentuserid(request); # get id of current user
	orgbugs = querybugs(id) # gets list of bugs from the organization belonging to the user whose ID is passed in
	bugs_json = json.loads(serializers.serialize("json", orgbugs)) # format that list of bugs and format it into JSON
	# bugs_json = "{\"name\":\"John\", \"age\":31, \"city\":\"New Yorkk\"}" # Dummy JSON for Debugging
	return JsonResponse(bugs_json, safe=False) # return that json object

# returns a list of bugs in list format, given id of a user
def querybugs(id):
	org_sel = orgofid(id) # get the organization of the current user
	org_sel_id = org_sel['org'] # get id of organization
	orgbugs = bug.objects.filter(org = org_sel_id) # grab a list of all bugs from that org
	return orgbugs

# returns id of organization of the user (user id) that is passed in
def orgofid(user_id):
	# Filter users by id passed in, then get the organization that the user belongs to
	org = User.objects.filter(id = user_id).values('org')
	return org[0] # only 1 value should be returned

# returns user id of the user who is currently logged in
def currentuserid(request):
	if not request.user.is_authenticated:
		return -1 # sends -1 if user is not logged in
	else:
		return request.user.id # otherwise sends user id

def bugdetailspage(request, bug_id):
	# print("bugdetailspage render: " + str(bug_id)) # This line is called, as expected
	return render(request, "bugtracker/bugdetailspage.html", {
		"bug_id": str(bug_id)
	})


def bugdetailcontent(request, bug_id):
	print("bugdetailcontent returning: " + str(bug_id)) # This line is called, as expected
	bug_sel = bug.objects.filter(id = bug_id)[0] # get first index
	data = {'title': str(bug_sel.title), 'description': str(bug_sel.description), 'severity': str(bug_sel.severity), 'estimate': str(bug_sel.estimate), 'sme': str(bug_sel.sme), 'org': str(bug_sel.org)}

	# data = "{\"name\":\"John\", \"age\":31, \"city\":\"New York\"}" # Dummy Data for Debugging
	return JsonResponse(data, safe=False)

def bugdetailedit(request, bug_id):
	return render(request, "bugtracker/bugeditpage.html", {
		"bug_id": str(bug_id)
	}) # error page for now

def createbug(request):
	if request.method == "POST":
		print("A post request was made to createbug def in views.py...")
		# TODO render the bug create form if debugging, otherwise render the list of bugs page

	current_user = request.user # gives current user id
	current_user_id = current_user.id # get id of current user
	orgs = User.objects.filter(id = current_user_id).values('org')[0]['org'] # gets the id organization that the user belongs to (request.user.id), then gets the first index of that([0]) and grabs the map of that ('org')
	users = User.objects.filter(org = orgs) # gets the users belonging to the org that is passed in

	bcf = bugCreateForm()
	bcf.fields['sme'].queryset = users
	return render(request, "bugtracker/createbug.html", {
		"form": bcf
	})

	# users = User.objects.filter(org = User.objects.filter(id = request.user.id).values('org')[0]['org']) # All logic combined
	# https://stackoverflow.com/questions/8841502/how-to-use-the-request-in-a-modelform-in-django
	# bcf.fields['sme'].queryset = User.objects.filter(org = User.objects.filter(id = request.user.id).values('org')[0]['org'])