
##CS50 Capstone: Bug Tracker

**Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.**
My final capstone project is a bug tracker.
It lets users track their bugs on team projects.

Bugs have the following details
* Titles
* Descriptions (Reproduction steps)
* Estimates (in hours)
* Subject Matter Expert (who is responsible for solvint the bug)
  * They can be one of several types/categories:
  * Functional
  * Performance
  * Usability
  * Compatability
  * Security
  * Other
* They can also have one of several severities:
  * Low
  * Medium
  * High
  * Critical
* Users can create and edit bugs,
They can also mark bugs complete.

**What’s contained in each file you created.**
Here are a following list of files by directories
* /bugtracker/
This contains all the python files used by the server.
	* admin.py
	This file is responsible for registering the models: User, bug, organization.
	* apps.py
	This file registers the following app: "bugtracker".
	* forms.py
	This file generates the form to create bugs, based off of the model for the "bug" object.
	* models.py
	This file holds a list of models for objects that are used by this application. Currently, there are 3 models:
		* 'organization': The organization object represents an organization that the user is part of. This  could be a company or just a group made for a group project. When a user logs in, they will see all bugs that are in that group; there is also a separate page for bugs that are assigned to them specifically.
		* 'User': The user object represents a user that has logged in, they have the ability to create, edit, and close bugs.
		* 'bug': "A software bug is an error, flaw or fault in a computer program or system that causes it to produce an incorrect or unexpected result, or to behave in unintended ways". This application allows groups to track bugs in any software that they are building.
	* tests.py
	This file was generate automatically when the app was created, but is not used.
	* urls.py
	This file contains all the different urls that are accessible by the user. Some of them are direct urls that lead to a webpage, however some of them are APIs that return a JSON object which are fed into Javascript on these webpages. 
	* views.py
	This file contains all the routes. Each url from the urls.py file calls a method from this file, which returns either a JSON (in the case of an api call)  or renders an html page.
* /bugtracker/static/bugtracker
This contains all the Javascript files
	* bugdetailspage.js
	* bugeditpage.js
	* buglist_react.js
	* createbug.js
	* userbuglist_react.js
	* vanilla_template.js
* /bugtracker/templates/bugtracker/

**How to run your application.**
1. Git clone this repository
2. 
  
**Any other additional information the staff should know about your project.**

There are no other dependencies.