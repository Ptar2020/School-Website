from . models import About_the_school
from django import forms

class SchoolEditForm(forms.ModelForm):
	class Meta:
		model = About_the_school
		fields = ("S_Name","S_Motto","Total","Streams","Zone",
			"County","Subcounty","Category","About_the_school",
			"Mission","Vision","Address","Sponsor")
		
		widgets = {
			"S_Name":forms.TextInput(attrs={"class":'form-control'}),
			"S_Motto":forms.TextInput(attrs={"class":'form-control'}),
			"Total":forms.TextInput(attrs={"class":'form-control'}),
			"Streams":forms.TextInput(attrs={"class":'form-control'}),
			"Zone":forms.TextInput(attrs={"class":'form-control'}),
			"County":forms.TextInput(attrs={"class":'form-control'}),
			"Subcounty":forms.TextInput(attrs={"class":'form-control'}),
			"Category":forms.TextInput(attrs={"class":'form-control'}),
			"About_the_school":forms.Textarea(attrs={"class":'form-control'}),
			"Sponsor":forms.TextInput(attrs={"class":'form-control'}),
			"Address":forms.TextInput(attrs={"class":'form-control'}),
			"Vision":forms.TextInput(attrs={"class":'form-control'}),
			"Mission":forms.TextInput(attrs={"class":'form-control'}),
		}

