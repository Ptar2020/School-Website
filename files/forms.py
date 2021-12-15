from django import forms
from .models import *

class AddDownloadsForm(forms.ModelForm):
	class Meta:
		model = Download
		fields = ("File",'File_Name')

		
		widgets = {
			"File":forms.FileInput(),
			"File_Name":forms.TextInput(attrs={"class":"form-control"}),
			
		}

class FileEditForm(forms.ModelForm):
	class Meta:
		model = Download
		fields = ("File_Name","File")
		
		widgets = {
			"File_Name":forms.TextInput(attrs={"class":'form-control'}),
			"File":forms.FileInput(),}