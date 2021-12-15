from django.db import models
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField


class EventsModel(models.Model):
	post_date = models.DateTimeField(auto_now_add=True)
	event_date = models.DateField()
	event_title = models.TextField(blank=True)
	event_description = RichTextField(blank=True)


	class Meta:
		ordering = ('-post_date','event_date')
	def __str__(self):
		return self.event_title