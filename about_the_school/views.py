from django.shortcuts import render, redirect
from .models import *
from . forms import SchoolEditForm
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin

def About_School(request):
	about_school = About_the_school.objects.all()
	return render(request, 'about_school.html',{'about_school':about_school})

class UpdateSchoolView(LoginRequiredMixin,UpdateView):
	login_url = 'login'
	model = About_the_school
	form_class = SchoolEditForm
	template_name = "edit_school.html"
	success_url = reverse_lazy('about_school')
class CreateSchoolView(LoginRequiredMixin,CreateView):
	login_url = 'login'
	model = About_the_school
	form_class = SchoolEditForm
	template_name = "create_school.html"
	success_url = reverse_lazy('about_school')