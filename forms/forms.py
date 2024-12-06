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

class ResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        form_instance = kwargs.pop('form_instance', None)
        super(ResponseForm, self).__init__(*args, **kwargs)

        if form_instance:
            for question in form_instance.questions.all():
                field_name = f'question_{question.id}'

                if question.question_type == 'short_answer':
                    self.fields[field_name] = forms.CharField(label=question.question_text)
                elif question.question_type == 'paragraph':
                    self.fields[field_name] = forms.CharField(label=question.question_text, widget=forms.Textarea)
                elif question.question_type == 'multiple_choice':
                    choices = [(choice.id, choice.choice_text) for choice in question.options.all()]
                    self.fields[field_name] = forms.ChoiceField(label=question.question_text, choices=choices,
                                                                widget=forms.RadioSelect)
                elif question.question_type == 'checkbox':
                    choices = [(choice.id, choice.choice_text) for choice in question.options.all()]
                    self.fields[field_name] = forms.MultipleChoiceField(label=question.question_text, choices=choices,
                                                                        widget=forms.CheckboxSelectMultiple)
                elif question.question_type == 'dropdown':
                    choices = [(choice.id, choice.choice_text) for choice in question.options.all()]
                    self.fields[field_name] = forms.ChoiceField(label=question.question_text, choices=choices,
                                                                widget=forms.Select)
                elif question.question_type == 'file_upload':
                    self.fields[field_name] = forms.FileField(label=question.question_text, required=False)
                elif question.question_type == 'date':
                    self.fields[field_name] = forms.DateField(label=question.question_text,
                                                              widget=forms.DateInput(attrs={'type': 'date'}),
                                                              required=False)
                elif question.question_type == 'time':
                    self.fields[field_name] = forms.TimeField(label=question.question_text,
                                                              widget=forms.TimeInput(attrs={'type': 'time'}),
                                                              required=False)