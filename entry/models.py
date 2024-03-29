from django.db import models

# Create your models here.
class Entry(models.Model):
	name = models.CharField(max_length=20)
	story = models.TextField()
	date = models.DateTimeField(auto_now_add=True, blank=True)
		
	def __str__(self):
		return self.name

	def snippet(self):
		return self.story[:100] + '...'