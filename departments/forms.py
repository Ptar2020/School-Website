from . models import DepartmentsModel
from django import forms


subjects = [('','--Choose Subject--'),
			('ENGLISH','ENGLISH'),('KISWAHILI','KISWAHILI'),
			('MATHS','MATHS'),('CHEMISTRY','CHEMISTRY'),
			('BIOLOGY','BIOLOGY'),('PHYSICS','PHYSICS'),('HISTORY','HISTORY'),
			('CRE','CRE'),('GEOGRAPHY','GEOGRAPHY'),('AGRICULTURE','AGRICULTURE'),
			('H/SCIENCE','H/SCIENCE'),('B/STUDIES','B/STUDIES'),
			('LITERATURE','LITERATURE'),('OTHER','OTHER')]
class DepartmentsForm(forms.ModelForm):
	class Meta:
		model = DepartmentsModel
		fields = ("Name_of_department","HOD","Assistant_1","Assistant_2","Assistant_3",
			"Assistant_4","Assistant_5","Assistant_6","Assistant_7",
			"Assistant_8","Assistant_9","Assistant_10","About",
			"Subject_1","Subject_2","Subject_3","Subject_4","Subject_5","Subject_6","Subject_7",'author',
			)	
		widgets = {
			'author':forms.TextInput(attrs={"class":'form-control','value':'','id':'identifier','type':'hidden'}),
			"Name_of_department":forms.TextInput(attrs={"class":'form-control'}),
			"HOD":forms.TextInput(attrs={"class":'form-control'}),
			"About":forms.Textarea(attrs={"class":'form-control'}),
			"Assistant_1":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_2":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_3":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_4":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_5":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_6":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_7":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_8":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_9":forms.TextInput(attrs={"class":'form-control'}),
			"Assistant_10":forms.TextInput(attrs={"class":'form-control'}),
			"Subject_1":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_2":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_3":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_4":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_5":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_6":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_7":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_8":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_9":forms.Select(choices=subjects,attrs={"class":'form-control'}),
			"Subject_10":forms.Select(choices=subjects,attrs={"class":'form-control'}),

			}
