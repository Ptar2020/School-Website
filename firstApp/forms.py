from . models import Contact,Photos,Teacher
from django import forms
from django.contrib.auth.models import User

first_subject = [('','--Select a subject--'),
				('ENGLISH','ENGLISH'),('KISWAHILI','KISWAHILI'),('MATHS','MATHS'),
				('CHEMISTRY','CHEMISTRY'),('BIOLOGY','BIOLOGY'),('PHYSICS','PHYSICS'),
				('GEOGRAPHY','GEOGRAPHY'),('HISTORY','HISTORY'),('CRE','CRE'),('MUSIC','MUSIC'),
				('FRENCH','FRENCH'),('COMPUTER','COMPUTER'),('B/STUDIES','B/STUDIES'),
				('H/SCIENCE','H/SCIENCE'),('AGRICULTURE','AGRICULTURE'),
				('LITERATURE','LITERATURE')]

second_subject = [('','--Select a subject--'),
				('ENGLISH','ENGLISH'),('KISWAHILI','KISWAHILI'),('MATHS','MATHS'),
				('CHEMISTRY','CHEMISTRY'),('BIOLOGY','BIOLOGY'),('PHYSICS','PHYSICS'),
				('GEOGRAPHY','GEOGRAPHY'),('HISTORY','HISTORY'),('CRE','CRE'),('MUSIC','MUSIC'),
				('FRENCH','FRENCH'),('COMPUTER','COMPUTER'),('B/STUDIES','B/STUDIES'),
				('H/SCIENCE','H/SCIENCE'),('AGRICULTURE','AGRICULTURE'),
				('LITERATURE','LITERATURE')]

employers = [('','--Choose Employer--'),
			('BOM','BOM'),('TSC','TSC'),
			('Intern','Intern'),('TP','TP'),('Other','Other')]

my_gender = [('', '--Choose gender--'),
			('Male','Male'),('Female','Female')]

designation = [('','--Choose Designation--'),
			('Principal','Principal'),('Deputy Principal','Deputy Principal'),
			('D.O.S','D.O.S'),('Class Teacher','Class Teacher'),
			('H.O.D','H.O.D'),('Teacher','Teacher')]

class ContactEditForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ("Phone_1","Phone_2","Email","Address","Twitter_url",
			"Instagram_url","Facebook_url","Other_url")
		
		widgets = {
			"Email":forms.EmailInput(attrs={"class":'form-control'}),
			"Phone_1":forms.TextInput(attrs={"class":'form-control'}),
			"Phone_2":forms.TextInput(attrs={"class":'form-control'}),
			"Address":forms.TextInput(attrs={"class":'form-control'}),
			"Twitter_url":forms.TextInput(attrs={"class":'form-control'}),
			"Instagram_url":forms.TextInput(attrs={"class":'form-control'}),
			"Facebook_url":forms.TextInput(attrs={"class":'form-control'}),
			"Other_url":forms.TextInput(attrs={"class":'form-control'}),
		}

class AddPhotosForm(forms.ModelForm):
	class Meta:
		model = Photos
		fields = ("Photo","Description")
		
		widgets = {
			"Photo":forms.FileInput(),
			"Description":forms.TextInput(attrs={"class":'form-control'}),}



class AddTeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ("Designation","Teachers_name","Teachers_photo","Teachers_first_subject",
			"Teachers_second_subject","Employer","Gender")

		widgets = {
			"Teachers_photo":forms.FileInput(),
			"Designation":forms.Select(choices=designation,attrs={"class":'form-control'}),
			"Teachers_name":forms.TextInput(attrs={"class":'form-control'}),
			"Teachers_first_subject":forms.Select(choices=first_subject,attrs={"class":'form-control'}),
			"Teachers_second_subject":forms.Select(choices=second_subject,attrs={"class":'form-control'}),
			"Employer":forms.Select(choices=employers,attrs={"class":'form-control'}),
			#"Gender":forms.TextInput(attrs={"class":'form-control'}),
			#"Gender":forms.CharField(max_length=70,label='gender',forms.Select(choices=my_gender)),
			"Gender":forms.Select(choices=my_gender,attrs={"class":'form-control'}),
			}

class UpdateTeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ("Designation","Teachers_name","Teachers_photo","Teachers_first_subject",
			"Teachers_second_subject","Employer","Gender")
		
		widgets = {
			"Teachers_photo":forms.FileInput(),
			"Designation":forms.Select(choices=designation,attrs={"class":'form-control'}),
			"Teachers_name":forms.TextInput(attrs={"class":'form-control'}),
			"Teachers_first_subject":forms.Select(choices=first_subject,attrs={"class":'form-control'}),
			"Teachers_second_subject":forms.Select(choices=second_subject,attrs={"class":'form-control'}),
			"Employer":forms.Select(choices=employers,attrs={"class":'form-control'}),
			#"Gender":forms.TextInput(attrs={"class":'form-control'}),
			"Gender":forms.Select(choices=my_gender,attrs={"class":'form-control'}),}

class AddUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email","password")
		
		widgets = {
			"username":forms.TextInput(attrs={"class":'form-control','placeholder':'Username'}),
			"first_name":forms.TextInput(attrs={"class":'form-control','placeholder':'Firs tname'}),
			"last_name":forms.TextInput(attrs={"class":'form-control','placeholder':'Last name'}),
			"email":forms.EmailInput(attrs={"class":'form-control','placeholder':'Email'}),
			"password":forms.PasswordInput(attrs={"class":'form-control','placeholder':'Password'}),}
class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("username","first_name","last_name","email","password")
		
		widgets = {
			"username":forms.TextInput(attrs={"class":'form-control','placeholder':'Username'}),
			"first_name":forms.TextInput(attrs={"class":'form-control','placeholder':'Firs tname'}),
			"last_name":forms.TextInput(attrs={"class":'form-control','placeholder':'Last name'}),
			"email":forms.EmailInput(attrs={"class":'form-control','placeholder':'Email'}),
			"password":forms.PasswordInput(attrs={"class":'form-control','placeholder':'Password'}),}
