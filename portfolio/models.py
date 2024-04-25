from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	name = models.CharField(max_length=200)
	d1 = models.CharField(max_length=200)
	d2 = models.CharField(max_length=200)

	def __str__(self):
		return self.name