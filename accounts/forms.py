from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Account

gender = [('Male','Male'),('Female','Female')]

class RegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','username','email', 'password1','password2')

	widgets = {
    'first_name' : forms.TextInput(attrs={"class":'form-control'}),
    'last_name' : forms.TextInput(attrs={"class":'form-control'}),
    'username' : forms.TextInput(attrs={"class":'form-control'}),
    'email' : forms.EmailInput(attrs={"class":'form-control'}),    
    'password1' : forms.PasswordInput(attrs={"class":'form-control'}),
    'password2' : forms.PasswordInput(attrs={"class":'form-control'}),
    }

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','username','email')

	widgets = {
    'first_name' : forms.TextInput(attrs={"class":'form-control'}),
    'last_name' : forms.TextInput(attrs={"class":'form-control'}),
    'username' : forms.TextInput(attrs={"class":'form-control'}),
    'email' : forms.EmailInput(attrs={"class":'form-control'}),
    }


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")


class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email', 'username', )

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)















