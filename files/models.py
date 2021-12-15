from django.db import models
from django.urls import reverse

class Download(models.Model):
	File = models.FileField(upload_to='files')
	File_Name = models.CharField(max_length=200)

	class Meta:
		ordering = ('-pk','File_Name')

	def get_absolute_url(self):
		return reverse('home')
	def __str__(self):
		return self.File_Name