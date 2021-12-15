from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import DepartmentsModel
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import DepartmentsForm

class DeparmentsDetailView(DetailView):

    model = DepartmentsModel
    template_name = 'department_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = DepartmentsModel.objects.all()
        return context

def DepartmentsView(request):
	departments = DepartmentsModel.objects.all()
	return render(request,'departments.html',{'departments':departments})

class UpdateDepartmentsView(LoginRequiredMixin,UpdateView):
	model = DepartmentsModel
	form_class = DepartmentsForm
	template_name = "edit_department.html"
	success_url = reverse_lazy('departments')

class CreateDepartmentsView(LoginRequiredMixin,CreateView):
	model = DepartmentsModel
	form_class = DepartmentsForm
	template_name = "create_department.html"
	success_url = reverse_lazy('departments')

class DeleteDepartmentsView(LoginRequiredMixin,DeleteView):
	model = DepartmentsModel
	template_name = 'delete_department.html'
	success_url = reverse_lazy('departments')

