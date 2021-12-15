from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField



my_gender = [
			('male','male'),
			('female','female')
			]
class Teacher(models.Model):
	Designation = models.CharField(max_length=100)
	Teachers_photo = models.ImageField(blank=True, null=True, upload_to='pics')
	Teachers_name = models.CharField(max_length=100)
	Teachers_first_subject = models.CharField(max_length=100)
	Teachers_second_subject = models.CharField(max_length=100)
	Employer = models.CharField(max_length=100)
	Gender = models.CharField(max_length=100)
	Record_updated_on = models.DateTimeField(auto_now_add=True)
	#gender = models.CharField(max_length=70,label='gender',model.Select(choices=my_gender))

	class Meta:
		ordering = ('Record_updated_on','Teachers_name')
	def __str__(self):
		return self.Designation

class Category(models.Model):
	name = models.CharField(max_length=255)

	def  __str__(self): 
		return self.name 

	def get_absolute_url(self):
		return reverse('home')

class Contact(models.Model):
	Phone_1 = models.CharField(max_length=200,blank=True)
	Phone_2 = models.CharField(max_length=200,blank=True)
	Email = models.EmailField(max_length=255,blank=True,null=True)
	Address = models.CharField(max_length=255,blank=True,null=True)
	Twitter_url = models.CharField(max_length=255,blank=True,null=True)
	Instagram_url = models.CharField(max_length=255,blank=True,null=True)
	Facebook_url = models.CharField(max_length=255,blank=True,null=True)
	Other_url = models.CharField(max_length=255,blank=True,null=True)
	def __str__(self):
		return('Contact')
class Photos(models.Model):
	Photo = models.ImageField(upload_to='background',blank=True,null=True)
	Description = RichTextField(blank=True,null=True)

	class Meta:
		ordering = ('-pk','Photo')
	def __str__(self):
		return('Photos')