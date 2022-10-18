# portfolio/models.py

from django.db import models

# Create your models here.

class Post(models.Model):
	"""Holds text/markdown related to personal posts"""
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	author_email = models.CharField(max_length=50)
	date = models.DateField(auto_now_add=True)
	text = models.CharField(max_length=2000)

	def __str__(self):
		return self.title


class ProjectDisplay(models.Model):
	"""Holds Links / Images related to personal projects"""
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	link = models.CharField(max_length=1000)

	def __str__(self):
		return self.name
