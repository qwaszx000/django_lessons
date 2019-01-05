from django.db import models

# Create your models here.

class question(models.Model):
	email = models.CharField(max_length = 256)
	question = models.TextField()

	def __str__(self):
		return self.email