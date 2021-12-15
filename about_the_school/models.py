from django.db import models
from ckeditor.fields import RichTextField

class About_the_school(models.Model):
	About_the_school = RichTextField(blank=True)
	S_Name = models.CharField(max_length=150,blank=True)
	S_Motto = models.CharField(max_length=150,blank=True)
	Total = models.CharField(max_length=150,blank=True)
	Streams = models.CharField(max_length=150,blank=True)
	Zone = models.CharField(max_length=150,blank=True)
	County = models.CharField(max_length=150,blank=True)
	Subcounty = models.CharField(max_length=150,blank=True)
	Category = models.CharField(max_length=150,blank=True)
	Sponsor = models.CharField(max_length=150,blank=True)
	Address = models.CharField(max_length=150,blank=True)
	Vision = models.CharField(max_length=150,blank=True)
	Mission = models.CharField(max_length=150,blank=True)

	def __str__(self):
		return('About FR. GULIK')
