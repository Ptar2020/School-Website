from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .forms import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

'''
def AddDownloadView(request):
    if request.method == 'POST':
        form = AddDownloadsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'all_downloads')
    else:
        form = AddDownloadsForm()
    return render(request, 'add_file.html', {'form': form})'''

def File_Download(request):
	file = Download.objects.all()
	return render(request,'downloads_view.html',{'file':file})

class Events_View(ListView):
	model = Download
	form_class = AddDownloadsForm
	template_name = 'events.html'

	def get_context_data(self, *args, **kwargs):
		events = Event.objects.all()
		context = super(Events_View,self).get_context_data(*args, **kwargs)
		context["events"] = events
		return context
class AddDownloadView(LoginRequiredMixin,CreateView):
	login_url = 'login'
	model = Download
	form_class = AddDownloadsForm
	template_name = 'add_file.html'
	success_url = reverse_lazy('all_downloads')

class UpdateDownloadView(LoginRequiredMixin,UpdateView):
	model = Download
	form_class = FileEditForm
	template_name = "edit_file.html"
	success_url = reverse_lazy('all_downloads')

class DeleteDownloadView(LoginRequiredMixin,DeleteView):
	model = Download
	template_name = "delete_file.html"
	success_url = reverse_lazy('all_downloads')