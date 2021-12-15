from django.urls import path
from .views import *

urlpatterns = [
	path('',Home, name='home'),
	path('teachers', Teachers, name='teachers'),
	path('admin_info', AdminView, name='administer'),
	path('contactinfo', Kontact, name='contact'),
	path('gallery', PhotoView.as_view(), name='photos'),
	path('manage_users', UsersView, name='users'),
	path('Search', SearchView, name='search'),
	path('photo<int:pk>', PhotoDetailView.as_view(),name='photo_detail'),
	
	#Generic views
	path('admin_details/<int:pk>',AdministerDetailView.as_view(), name='admin_detail'),
	path('edit_contact/<int:pk>',UpdateContactView.as_view(), name='update_contact'),
	path('delete_photos/<int:pk>',DeletePhotosView.as_view(), name='delete_photos'),
	path('edit_photos/<int:pk>',UpdatePhotosView.as_view(), name='update_photos'),
	path('add_photo',AddPhotosView.as_view(), name='add_photo'),
	path('add_teacher',AddTeacherView.as_view(), name='add_teacher'),
	path('teacher-details/<int:pk>',TeacherDetailView.as_view(), name='teacher_detail'),
	path('delete_teacher/<int:pk>',DeleteTeacherView.as_view(), name='delete_teacher'),
	path('edit_teacher/<int:pk>',UpdateTeacherView.as_view(), name='update_teacher'),
	path('add_user',AddUserView.as_view(), name='add_user'),
	path('edit_user/<int:pk>',UpdateUserView.as_view(), name='update_user'),
	path('delete_user/<int:pk>',DeleteUserView.as_view(), name='delete_user'),

	path('create_contact',CreateContactView.as_view(), name='create_contact'),
    ]