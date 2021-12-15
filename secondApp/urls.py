from django.urls import path
from .views import CreateAdministerView,UpdateAdministerView,DeleteAdministerView

urlpatterns = [
	
	path('new_administrator',CreateAdministerView.as_view(),name='add_administer'),
	path('edit_administrator/<int:pk>',UpdateAdministerView.as_view(),name='edit_administer'),
	path('delete_administrator/<int:pk>',DeleteAdministerView.as_view(),name='delete_administer'),

    ]