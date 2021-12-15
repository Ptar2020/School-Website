from django.db import models
from django.urls import reverse_lazy,reverse

class Display_Photo(models.Model):
	photo1 = models.ImageField(upload_to='photos', null=True, blank=True)
	photo1_Description = models.CharField(max_length=50,blank=True)
	photo2 = models.ImageField(upload_to='photos', null=True, blank=True)
	photo2_Description = models.CharField(max_length=50,blank=True)
	photo3 = models.ImageField(upload_to='photos', null=True, blank=True)
	photo3_Description = models.CharField(max_length=50,blank=True)
	photo4 = models.ImageField(upload_to='photos', null=True, blank=True)
	photo4_Description = models.CharField(max_length=50,blank=True)
	photo5 = models.ImageField(upload_to='photos', null=True, blank=True)
	photo5_Description = models.CharField(max_length=50,blank=True)

	class Meta:
		ordering = ('-pk','photo1')

	def get_absolute_url(self):
		return reverse('back_photos')
	def __str__(self):
		return('Photos')