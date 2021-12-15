from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from . models import *
from . forms import (ContactEditForm,AddPhotosForm,AddTeacherForm,
	UpdateTeacherForm,AddUserForm,UpdateUserForm)
from eventuals.models import *
from secondApp.models import *
from files.models import *
from background_photos.models import *
from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm,UserEditForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from departments.models import DepartmentsModel



def SearchView(request):
	querry = request.GET.get('q','')
	if querry:
		querryset1 = (Q(Employer__icontains=querry))|(Q(Gender__icontains=querry))|\
		(Q(Teachers_name__icontains=querry))|(Q(Teachers_first_subject__icontains=querry))|\
		(Q(Teachers_second_subject__icontains=querry))|(Q(Designation__icontains=querry))
		
		querryset2 = (Q(Phone_1__icontains=querry))
		querryset3 = (Q(File_Name__icontains=querry))

		results1 = Teacher.objects.filter(querryset1).distinct()
		results2 = Contact.objects.filter(querryset2).distinct()
		results3 = Download.objects.filter(querryset3).distinct()
		names = {'results1':results1,'results2':results2,'querry':querry,'results3':results3}
	else:
		names =  {}#messages.success(request, f'Nothing to search...')
		
	return render(request,'search_results.html',names )

class PhotoView(ListView):
	model = Photos 
	template_name = 'photos.html'

	def get_context_data(self, *args, **kwargs):
		photos = Display_Photo.objects.all()
		context = super(PhotoView,self).get_context_data(*args, **kwargs)
		context['photos'] = photos
		return context
	paginate_by = 6
'''
class PhotoDetailView(DetailView):
	model = Photos
	template_name = 'photo_detail.html'

	def get_context_data(self, *args, **kwargs):
		photos = Display_Photo.objects.all()
		context = super(PhotoDetailView,self).get_context_data(*args, **kwargs)
		context["photos"] = photos
		return context'''

class PhotoDetailView(DetailView):

    model = Photos
    template_name = 'photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Display_Photo.objects.all()
        return context

def AdminView(request):
	administer = AdminModel.objects.all()
	return render(request, 'home.html', {'administer':administer})

class AdministerDetailView(DetailView):

    model = AdminModel
    template_name = 'admin_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admin'] = AdminModel.objects.all()
        return context


def Home(request):
	administer = AdminModel.objects.all()
	file = Download.objects.all()
	events = EventsModel.objects.all()
	photos = Display_Photo.objects.all()

	return render(request, 'home.html',
		{'events':events,
		'file':file,
		"photos":photos,
		"administer":administer,
		})


def Teachers(request):
	items = Teacher.objects.all()
	return render(request, 'teachers.html',{"items":items})
	#ordering = ['-Record_updated_on']

class TeacherDetailView(DetailView):

    model = Teacher
    template_name = 'teacher_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Teacher.objects.all()
        return context


'''
def PhotoView(request):
	photos = Photos.objects.all()
	return render(request, 'photos.html',{'photos':photos})'''
class AddPhotosView(LoginRequiredMixin,CreateView):
	model = Contact
	form_class = AddPhotosForm
	template_name = "add_photo.html"
	success_url = reverse_lazy('photos')

class DeletePhotosView(LoginRequiredMixin,DeleteView):
	model = Photos
	template_name = "delete_photo.html"
	success_url = reverse_lazy('photos')

class UpdatePhotosView(LoginRequiredMixin,UpdateView):
	model = Photos
	form_class = AddPhotosForm
	template_name = "edit_photos.html"
	success_url = reverse_lazy('photos')


def Kontact(request):
	contacts = Contact.objects.all()
	return render(request, 'contact.html',{"contacts":contacts})
class UpdateContactView(LoginRequiredMixin,UpdateView):
	model = Contact
	form_class = ContactEditForm
	template_name = "edit_contact.html"
	success_url = reverse_lazy('contact')

class CreateContactView(LoginRequiredMixin,CreateView):
	model = Contact
	form_class = ContactEditForm
	template_name = "create_contact.html"
	success_url = reverse_lazy('contact')
class AddTeacherView(LoginRequiredMixin,CreateView):
	model = Teacher
	form_class = AddTeacherForm
	template_name = 'add_teacher.html'
	success_url = reverse_lazy('teachers')

#Views for the users

@login_required(login_url= 'login')
def UsersView(request):
	users = User.objects.all()
	return render(request,'users.html',{'users':users})

class UpdateTeacherView(LoginRequiredMixin,UpdateView):
	model = Teacher
	form_class = UpdateTeacherForm
	template_name = "edit_teacher.html"
	success_url = reverse_lazy('teachers')

class DeleteTeacherView(LoginRequiredMixin,DeleteView):
	model = Teacher
	template_name = "delete_teacher.html"
	success_url = reverse_lazy('teachers')

class AddUserView(LoginRequiredMixin,CreateView):
	model = User
	form_class = RegistrationForm#AddUserForm
	template_name = 'add_user.html'
	success_url = reverse_lazy('home')

class UpdateUserView(LoginRequiredMixin,UpdateView):
	model = User
	form_class = UserEditForm
	template_name = 'edit_user.html'
	success_url = reverse_lazy('home')

class DeleteUserView(LoginRequiredMixin,DeleteView):
	model = User
	template_name = 'delete_user.html'
	success_url = reverse_lazy('users')