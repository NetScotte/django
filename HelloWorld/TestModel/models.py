from django.db import models

# Create your models here.

class Test(models.Model):
	name = models.CharField(max_length=20)
	
	def __str__(self):
		info= str(self.id) + "\t" + self.name
		return info