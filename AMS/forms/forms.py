from django import forms
from .models import *

class PlayerForm(forms.ModelForm):
	team = forms.ModelChoiceField(queryset=Team.objects.all(), label="Select Team")

	class Meta:
		model = Player
		fields = '__all__'

# create form stuff

class CreateForm(forms.ModelForm):
	class Meta:
		model = Form
		fields = ['title', 'description']