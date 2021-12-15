from django.urls import path
from .views import (Add_Event_View, 
					UpdateEventView,
					DeleteEventView,
					EventsDetailView)

urlpatterns = [
	path('add_event',Add_Event_View.as_view(), name='add_event'),
	path('update_event/<int:pk>',UpdateEventView.as_view(), name='update_event'),
	path('delete_event/<int:pk>',DeleteEventView.as_view(), name='delete_event'),
	path('event_details/<int:pk>',EventsDetailView.as_view(), name='event_details'),
    ]