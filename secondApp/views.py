from django.shortcuts import render, redirect
from .models import AdminModel
from django.views.generic import UpdateView, CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from .forms import EditAdministerForm


class CreateAdministerView(LoginRequiredMixin, CreateView):
	model = AdminModel
	form_class = EditAdministerForm
	template_name = "create_administer.html"
	success_url = reverse_lazy('home')

class UpdateAdministerView(LoginRequiredMixin,UpdateView):
	model = AdminModel
	form_class = EditAdministerForm
	template_name = 'edit_administer.html'
	success_url = reverse_lazy('home')

class DeleteAdministerView(LoginRequiredMixin,DeleteView):
	model = AdminModel
	template_name = 'delete_administer.html'
	success_url = reverse_lazy('home')