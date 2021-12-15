from django.db import models

# Create your models here.
class PayfeeModel(models.Model):
	pay = models.CharField(max_length=250)

	def __str__(self):
		return self.pay