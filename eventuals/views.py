from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from . forms import Add_Event_Form,EditForm
from django.contrib.auth.mixins import LoginRequiredMixin



class Add_Event_View(LoginRequiredMixin,CreateView):
	model = EventsModel
	form_class = Add_Event_Form
	template_name = 'add_event.html'
	success_url = reverse_lazy('home')

class UpdateEventView(LoginRequiredMixin,UpdateView):
	model = EventsModel
	form_class = EditForm
	template_name = "edit_event.html"
	success_url = reverse_lazy('home')

class DeleteEventView(LoginRequiredMixin,DeleteView):
	model = EventsModel
	template_name = "delete_event.html"
	success_url = reverse_lazy('events')

class EventsDetailView(DetailView):

    model = EventsModel
    template_name = 'events_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = EventsModel.objects.all()
        return context
'''
def Events_View(request):
	events = Event.objects.all()
	return render(request, 'events.html',{'events':events})

class Event(CreateView):
	model = Event
	form_class = Add_Event_Form
	template_name = 'events.html'

	def get_context_data(self, *args, **kwargs):
		events = Event.objects.all()
		context = super(Event,self).get_context_data(*args, **kwargs)
		context["events"] = events
		return context'''
'''
class Events_View(ListView):
	model = Event
	template_name = 'events.html'
	success_url = reverse_lazy('home')

class Add_Event_View(CreateView):
	model = Event
	form_class = Add_Event_Form
	template_name = 'add_event.html'
	success_url = reverse_lazy('home')

class Add_Event_View(CreateView):
	model = Event
	form_class = Add_Event_Form
	template_name = 'add_event.html'

	def get_context_data(self, *args, **kwargs):
		events = Event.objects.all()
		context = super(Add_Event_View,self).get_context_data(*args, **kwargs)
		context["events"] = events
		return context


class Events_View(ListView):
	model = EventsModel
	form_class = Add_Event_Form
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		events = EventsModel.objects.all()
		context = super(Events_View,self).get_context_data(*args, **kwargs)
		context["events"] = events
		return context
		'''


