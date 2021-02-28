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
	# orgbugs = bug.objects.filter(org = org_sel_id) # grab a list of all bugs from that org
	orgbugs = bug.objects.filter(org = org_sel_id).filter(active = True) # grab a list of all bugs from that org that are active
	
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

def createbug(request):
	if request.method == "POST":
		form = bugCreateForm(request.POST)
		if form.is_valid():
			return_title = form.cleaned_data["title"]
			return_description = form.cleaned_data["description"]
			return_type = form.cleaned_data["type"]
			return_severity = form.cleaned_data["severity"]
			return_estimate = form.cleaned_data["estimate"]
			return_sme = form.cleaned_data["sme"]
			return_org = organization.objects.filter(id = getOrg(request))[0] # Get ID of Org that the user belongs to
			
			# For debugging
			log_form = "TITLE: " + str(return_title)
			log_form += "\nDESCRIPTION: " + str(return_description)
			log_form += "\nTYPE: " + str(return_type)
			log_form += "\nSEVERITY: " + str(return_severity)
			log_form += "\nESTIMATE: " + str(return_estimate)
			log_form += "\nSME: " + str(return_sme)
			log_form += "\nORG: " + str(return_org) 
			print(log_form)	

			# Create bug, and save it
			newbug = bug(title=return_title, description=return_description, type=return_type, severity=return_severity, estimate=return_estimate, sme=return_sme, org=return_org)
			newbug.save()

			return render(request, "bugtracker/buglistpage.html") # return buglistpage
		else:
			print("An invalid form was submitted...")
			print("ERRORS: " + str(form.errors))
			return render(request, "bugtracker/error.html")
	else: # Present user with a new form
		users = User.objects.filter(org = getOrg(request)) # gets the users belonging to the org that is passed in

		bcf = bugCreateForm()
		bcf.fields['sme'].queryset = users
		return render(request, "bugtracker/createbug.html", {
			"form": bcf
		})

def bugdetailedit(request, bug_id):
	if request.method == "POST":
		form = bugCreateForm(request.POST)
		if form.is_valid():
			return_title = form.cleaned_data["title"]
			return_description = form.cleaned_data["description"]
			return_type = form.cleaned_data["type"]
			return_severity = form.cleaned_data["severity"]
			return_estimate = form.cleaned_data["estimate"]
			return_sme = form.cleaned_data["sme"]
			return_org = organization.objects.filter(id = getOrg(request))[0] # Get ID of Org that the user belongs to
			
			# For debugging
			log_form = "TITLE: " + str(return_title)
			log_form += "\nDESCRIPTION: " + str(return_description)
			log_form += "\nTYPE: " + str(return_type)
			log_form += "\nSEVERITY: " + str(return_severity)
			log_form += "\nESTIMATE: " + str(return_estimate)
			log_form += "\nSME: " + str(return_sme)
			log_form += "\nORG: " + str(return_org) 
			print(log_form)	

			# Assign edited values to the bug
			bug_sel = bug.objects.filter(id = bug_id)[0]
			bug_sel.title = return_title
			bug_sel.description = return_description
			bug_sel.type = return_type
			bug_sel.severity = return_severity
			bug_sel.estimate = return_estimate
			bug_sel.sme = return_sme
			bug_sel.save() # save

			# Render page, which has now been edited
			return render(request, "bugtracker/bugdetailspage.html", {
				"bug_id": str(bug_id)
			})
	else:
		users = User.objects.filter(org = getOrg(request)) # gets the users belonging to the org that is passed in
		bug_sel = bug.objects.filter(id = bug_id)[0] # the bug that is being edited, get the first index of it

		# Create map to prepopulate fields
		data = {'title': bug_sel.title,
				'description': bug_sel.description,
				'type': bug_sel.type,
				'severity': bug_sel.severity,
				'estimate': bug_sel.estimate,
				'sme': bug_sel.sme}
		bcf = bugCreateForm(data) # pass in map to form to prepopulate fields
		bcf.fields['sme'].queryset = users # 
		return render(request, "bugtracker/bugeditpage.html", {
			"bug_id": str(bug_id), "form": bcf
		})

def getOrg(request): # Using the 'request' parameter, the organization that the user belongs to will be fetched and returned
	current_user = request.user # gives current user id
	current_user_id = current_user.id # get id of current user
	orgs = User.objects.filter(id = current_user_id).values('org')[0]['org'] # gets the id organization that the user belongs to (request.user.id), then gets the first index of that([0]) and grabs the map of that ('org')
	return orgs
	# users = User.objects.filter(org = User.objects.filter(id = request.user.id).values('org')[0]['org']) # All logic combined
	# https://stackoverflow.com/questions/8841502/how-to-use-the-request-in-a-modelform-in-django
	# bcf.fields['sme'].queryset = User.objects.filter(org = User.objects.filter(id = request.user.id).values('org')[0]['org'])

def usermessagecount(request): # returns json with count of total bugs assigned to org, and total bugs assigned to user
	current_user = request.user # gives current user id
	current_user_id = current_user.id # get id of current user
	orgs = User.objects.filter(id = current_user_id).values('org')[0]['org']
	# print(orgs) # gets the id organization that the user belongs to (request.user.id)
	
	# bugs_org = bug.objects.filter(org = orgs) # list of bugs that belong to that organization
	bugs_org = bug.objects.filter(org = orgs).filter(active = True) # list of bugs that belong to that organization
	# print(bugs_org.count())
	
	# bugs_user = bug.objects.filter(sme = current_user_id) # list of bugs that belong to user
	bugs_user = bug.objects.filter(sme = current_user_id).filter(active = True) # list of bugs that belong to user
	# print(bugs_user)
	
	bugs_json_2 = {'userbugs':str(bugs_user.count()), 'orgbugs':str(bugs_org.count())}  # Dummy JSON for Debugging Founder
	return JsonResponse(bugs_json_2, safe=False) # return that json object

def completebug(request, bug_id):
	# print("completebug method called for bug ID: " + str(bug_id))
	bug_sel = bug.objects.filter(id = bug_id)[0] # grabs bug that has id 
	print(str(bug_sel))
	bug_sel.active = False
	bug_sel.save()

	data = "{\"name\":\"John\", \"age\":31, \"city\":\"New York\"}"  # Dummy Data for Debugging
	data = {'bugid': bug_id}
	return JsonResponse(data, safe=False)
	# return render(request, "bugtracker/buglistpage.html") # does not go to url through button