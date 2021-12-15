from django.urls import path
from .views import UpdateSchoolView,About_School,CreateSchoolView

urlpatterns = [
	path('about',About_School, name="about_school"),
	path('editInfo/<int:pk>',UpdateSchoolView.as_view(),name='update_school'),
	path('createInfo/',CreateSchoolView.as_view(),name='create_school'),

    ]