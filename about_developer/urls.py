from django.urls import path
from .views import *

urlpatterns = [
	path('developer',About_Dev, name="about_dev"),

    ]