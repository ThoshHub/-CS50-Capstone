from django.forms import ModelForm
from django import forms
from .models import bug, BUG_SEVERITY, BUG_TYPES

class bugCreateForm(ModelForm):
	title = forms.Charfield(widget=forms.TextInput(
		attrs = {
			'class': 'form-control'
		}
	))

	description = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control'
		}
	))

	type = forms.CharField(widget=forms.Select(
		choices=tuple(list(BUG_SEVERITY.BUG_SEVERITY)),
		attrs={
			'class': 'form-control'
		}
	))

	severity = forms.CharField(widget=forms.Select(
		choices=tuple(list(BUG_TYPES.BUG_TYPES)),
		attrs={
			'class': 'form-control'
		}
	))

	estimate = forms.IntegerField(widget=forms.NumberInput(
		attrs={
			'class': 'form-control'
		}
	))

	# org is defined by default

	sme = forms.CharField(widget=forms.Select(
		choices=[('TODO', 'TODO')],
		attrs={
			'class': 'form-control'
		}
	))