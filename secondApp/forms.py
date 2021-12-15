from django import forms
from .models import AdminModel

counties = 		[('','--Choose County--'),('Siaya','Siaya'),('Kakamega','Kakamega'),('Kisii','Kisii'),
				('Busia','Busia')]
gender = 		[('Male','Male'),('Female','Female')]

designation = [('','--Choose Designation--'),
			('Principal','Principal'),('Deputy Principal','Deputy Principal'),
			('D.O.S','D.O.S'),('Class Teacher','Class Teacher'),
			('H.O.D','H.O.D'),('Teacher','Teacher'),('Senior Teacher','Senior Teacher'),
			('Board Member','Board Member'),('Board Chair','Board Chair'),('Other','Other')]

class EditAdministerForm(forms.ModelForm):
	class Meta:
		model = AdminModel
		fields = ("Designation","Name","Home_County","gender","Photo","About")
		
		widgets = {
			"Home_County":forms.Select(choices=counties,attrs={"class":'form-control'}),
			"About":forms.Textarea(attrs={"class":'form-control'}),
			"Name":forms.TextInput(attrs={"class":'form-control'}),
			"Photo":forms.FileInput(),
			"gender":forms.RadioSelect(choices=gender),
			"Designation":forms.Select(choices=designation,attrs={"class":'form-control'}),}

