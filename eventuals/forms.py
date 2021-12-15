from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})
from .models import EventsModel


class Add_Event_Form(forms.ModelForm):
	class Meta:
		model = EventsModel
		fields = ("event_date","event_title","event_description")
		
		widgets = {
			"event_date":forms.DateInput(attrs={'class':'datepicker form-control'}),
			#"event_date":forms.TextInput(attrs={"class":'form-control','placeholder':'Date of event'}),
			"event_title":forms.TextInput(attrs={"class":'form-control','placeholder':'Title of the event'}),
			"event_description":forms.Textarea(attrs={"class":'form-control','placeholder':'Event description'}),
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = EventsModel
		fields = ("event_date","event_title","event_description")
		
		widgets = {
			"event_date":forms.DateInput(attrs={'class':'datepicker  form-control'}),
			"event_title":forms.TextInput(attrs={"class":'form-control','placeholder':'Title of the event'}),
			"event_description":forms.Textarea(attrs={"class":'form-control','placeholder':'Event description'}),
		}