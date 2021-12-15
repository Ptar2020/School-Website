from django.shortcuts import render
from . models import MarqueeModel
from . forms import MarqueeEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,UpdateView,DeleteView,CreateView,DetailView
from django.urls import reverse_lazy,reverse

def Scroll(request):
	marquee = MarqueeModel.objects.all()
	return render(request, 'home.html', {'marquee':marquee})

class CreateMarqueeView(LoginRequiredMixin,CreateView):
	model = MarqueeModel
	form_class = MarqueeEditForm
	template_name = "create_marquee.html"
	success_url = reverse_lazy('home')

class UpdateMarqueeView(LoginRequiredMixin,UpdateView):
	model = MarqueeModel
	form_class = MarqueeEditForm
	template_name = "update_marquee.html"
	success_url = reverse_lazy('home')