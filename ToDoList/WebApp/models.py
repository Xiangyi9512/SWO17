from django.db import models

# Create your models here.

class Users(models.Model):
	username = models.CharField(max_length = 30, blank=False)
	password = models.CharField(max_length = 15, blank=False)
	def __str__(self):
		return self.username

class ToDoList(models.Model):
	user = models.ForeignKey(Users)
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date = models.DateTimeField('date created')
	def __str__(self):
		return '%s\n%s\n%s' % (self.date, self.title, self.content)