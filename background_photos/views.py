from django.shortcuts import render
from . models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import PhotosEditForm
from django.views.generic import UpdateView, CreateView
from django.urls import reverse_lazy,reverse

def Back_Photos(request):
	photos = Display_Photo.objects.all()
	return render(request, 'home.html',{"photos":photos})
def Back_Photos2(request):
	bphotos = Display_Photo.objects.all()
	return render(request, 'backgrounds.html',{"bphotos":bphotos})

def BackgroundView(request):
	backgrounds = Display_Photo.objects.all()
	return render(request, 'background.html',{"backgrounds":backgrounds})

class BackgroundView(LoginRequiredMixin,UpdateView):
	login_url = 'login'
	model = Display_Photo
	form_class = PhotosEditForm
	template_name = 'edit_backgrounds.html'
	success_url = reverse_lazy('bphotos')
class BackgroundCreateView(LoginRequiredMixin,CreateView):
	login_url = 'login'
	model = Display_Photo
	form_class = PhotosEditForm
	template_name = 'create_bg.html'
	success_url = reverse_lazy('bphotos')
