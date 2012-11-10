#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	name = models.CharField(max_length=20, unique=True)
  	description = models.TextField(help_text='Description of the company')
  	area = models.TextField(verbose_name='Area of work(IT,banking..)')
  	image = models.ImageField(upload_to='companies', verbose_name='Image')
  	register_time = models.DateTimeField(auto_now=True)
  	user = models.ForeignKey(User)
	
  	def __unicode__(self):
      		return self.name

class Comment(models.Model):
	company=models.ForeignKey(Company)
	text=models.TextField(help_text='Your comment', verbose_name='Comment')

	def __unicode__(self):
		return self.text
