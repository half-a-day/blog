from django.db import models

# Create your models here.
class Comments(models.Model):
	name = models.CharField(max_length=100)
	text = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)
	post = models.ManyToManyField('main.Post',blank=True)

	def __str__(self):
		return self.text[:10]