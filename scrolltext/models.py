from django.db import models
from ckeditor.fields import RichTextField

class MarqueeModel(models.Model):
	scroll_text = RichTextField(blank=True,null=True)
	def __str__(self):
		return f"This is scroll text"

