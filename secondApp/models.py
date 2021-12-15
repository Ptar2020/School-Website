from django.db import models
from ckeditor.fields import RichTextField

class AdminModel(models.Model):
	Designation = models.CharField(max_length=100,blank=True,null=True,default='Teacher')
	Photo = models.ImageField(upload_to='photos',blank=True,null=True)
	Name = models.CharField(max_length=100,blank=True,null=True)
	About = RichTextField(blank=True,null=True)
	Home_County = models.CharField(max_length=100,blank=True,null=True)
	gender = models.CharField(max_length=105,blank=True,null=True)
	def __str__(self):
		return self.Name + ' || ' + self.Designation