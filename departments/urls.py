from django.urls import path

from .views import (DepartmentsView,CreateDepartmentsView,UpdateDepartmentsView,DeparmentsDetailView,DeleteDepartmentsView)

urlpatterns = [
	
	path('view_departments',DepartmentsView,name='departments'),

	path('create_department',CreateDepartmentsView.as_view(),name='create_department'),
	
	path('edit_department/<int:pk>',UpdateDepartmentsView.as_view(),name='edit_department'),
	
	path('department_details/<int:pk>',DeparmentsDetailView.as_view(),name='department_details'),

	path('delete_department/<int:pk>',DeleteDepartmentsView.as_view(),name='delete_department'),


    ]