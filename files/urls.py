from django.urls import path
from .views import (AddDownloadView,UpdateDownloadView,DeleteDownloadView,File_Download)

urlpatterns = [
	path('downloads',File_Download, name='all_downloads'),
	path('add_file',AddDownloadView.as_view(),name='add_file'),
	#path('add_file',AddDownloadView,name='add_file'),
	path('update_file/<int:pk>',UpdateDownloadView.as_view(),name='update_file'),
	path('delete_file/<int:pk>',DeleteDownloadView.as_view(),name='delete_file'),

    ]