from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class organization(models.Model):
	name = models.CharField(null=True, max_length=128)
	def __str__(self): 
		# return f"{self.id}: {self.name}"
		return f"{self.name}"

class User(AbstractUser):
	org = models.ForeignKey(organization, on_delete=models.CASCADE, related_name="patron", blank=False, null=True)
	# test = models.CharField(null=True, max_length=128)

class BUG_TYPES: # bug types
	BUG_TYPES = [
		# (None, ''),
		('Functional','Functional'),
		('Performance', 'Performance'),
		('Usability','Usability'),
		('Compatability','Compatability'),
		('Security', 'Security'),
		('Other','Other'),
	]

class BUG_SEVERITY: # bug types
	BUG_SEVERITY = [
		# (None, ''),
		('Low','Low'),
		('Medium', 'Medium'),
		('High','High'),
		('Critical','Critical'),
	]

class bug(models.Model):
	title = models.CharField(null=True, max_length=128)
	description = models.CharField(null=True, max_length=128)
	type = models.CharField(
		max_length=13
		,choices=BUG_TYPES.BUG_TYPES
		,default=None
		,blank=True
		,null=True # TODO might want to delete this
	)
	severity = models.CharField(
		max_length=13
		,choices=BUG_SEVERITY.BUG_SEVERITY
		,default=None
		,blank=True
		,null=True # TODO might want to delete this
	)
	estimate = models.PositiveIntegerField(null=False)
	sme = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "owner", blank=False, null=False) # sme = subject matter expert
	org = models.ForeignKey(organization, on_delete=models.CASCADE, related_name="error", blank=False, null=True)
	active = models.BooleanField(default=True, blank=True) # active = whether the bug is active or not, true means it is active, false means it has been closed
	# blank determines whether the field will be required in forms. This includes the admin and your custom forms. If blank=True then the field will not be required, whereas if it's False the field cannot be blank.

	def __str__(self): 
		return f"{self.id}: {self.title}"