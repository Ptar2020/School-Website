from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *


from django.contrib.auth.models import User, auth
from django.contrib import messages

#Handles the Login page
def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request,'Invalid Credentials')
			return redirect('login')

	else:
		return render(request, 'login.html')

	return redirect('/')
'''
#Handles the registration page
def Register(request):
	#Handles the receipt/capture of information from the form
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password']
		password2 = request.POST['password_confirmation']
		#Authentification process
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username already taken, try again...')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email already registered. Try another email')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
				user.save();
				messages.info(request,'Successfull')
		else:
			messages.info(request,'Sorry, the passwords do not match...')
			return redirect('register')
	#Handles the submission of information to the page
	else:
		return render(request, 'register.html')
	return redirect('login') '''

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm


def Register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password1 = form.cleaned_data.get('password1')
            messages.success(request, f'An account has successfully been created for {first_name} {last_name}. Username is {username} and password is {password1}')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def Logout(request):
	auth.logout(request)
	return redirect('/')