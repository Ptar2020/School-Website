from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class DepartmentsModel(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	Name_of_department = models.CharField(max_length=100)
	HOD = models.CharField(max_length=100,blank=True,null=True)
	Subject_1 = models.CharField(max_length=100,blank=True,null=True)
	Subject_2 = models.CharField(max_length=100,blank=True,null=True)
	Subject_3 = models.CharField(max_length=100,blank=True,null=True)
	Subject_4 = models.CharField(max_length=10,blank=True,null=True)
	Subject_5 = models.CharField(max_length=100,blank=True,null=True)
	Subject_6 = models.CharField(max_length=100,blank=True,null=True)
	Subject_7 = models.CharField(max_length=100,blank=True,null=True)
	Assistant_1 = models.CharField(max_length=100,blank=True,null=True)
	Assistant_2 = models.CharField(max_length=100,blank=True,null=True)
	Assistant_3 = models.CharField(max_length=100,blank=True,null=True)
	Assistant_3= models.CharField(max_length=100,blank=True,null=True)
	Assistant_4= models.CharField(max_length=100,blank=True,null=True)
	Assistant_5= models.CharField(max_length=100,blank=True,null=True)
	Assistant_6= models.CharField(max_length=100,blank=True,null=True)
	Assistant_7= models.CharField(max_length=100,blank=True,null=True)
	Assistant_8= models.CharField(max_length=100,blank=True,null=True)
	Assistant_9= models.CharField(max_length=100,blank=True,null=True)
	Assistant_10= models.CharField(max_length=100,blank=True,null=True)
	About = RichTextField(blank=True,null=True)
	def __str__(self):
		return('Departments')
