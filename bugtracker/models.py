from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class organization(models.model):
    name = models.CharField(null=True, max_length=128)

class User(AbstractUser):
	org = models.ForeignKey(organization, on_delete=models.CASCADE, related_name= "employer", default=None, blank=True, null=True)

class BUG_TYPES: # bug types
	BUG_TYPES = [
		# (None, ''),
		('FUNCTIONAL','Functional'),
		('PERFORMANCE', 'Performance'),
		('USABILITY','Usability'),
		('COMPATABILITY','Compatability'),
        ('SECURITY', 'Security')
		('OTHER','Other'),
	]

class BUG_SEVERITY: # bug types
	BUG_SEVERITY = [
		# (None, ''),
		('LOW','Low'),
		('MEDIUM', 'Medium'),
		('HIGH','High'),
		('CRITICAL','Critical'),
	]

class bug(models.model):
    title = models.CharField(null=True, max_length=128)
    description = models.CharField(null=True, max_length=128)
    type = models.CharField(
		max_length=11
		,choices=BUG_TYPES.BUG_TYPES
		,default=None
		,blank=True
		,null=True # TODO might want to delete this
	)
    severity = models.CharField(
		max_length=11
		,choices=BUG_SEVERITY.BUG_SEVERITY
		,default=None
		,blank=True
		,null=True # TODO might want to delete this
	)
    estimate = models.PositiveIntegerField(null=False)
    sme = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "owner", default=None, blank=True, null=True) # sme = subject matter expert
    