from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Users(models.Model):
	name=models.CharField(max_length=30)
	password=models.CharField(max_length=30)
	email = models.EmailField()
	pic = models.CharField(max_length=125)

	def __unicode__(self):
		return self.name

class Tags(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class Article(models.Model):
	content = models.CharField(max_length=1000)
	time = models.DateField(default=timezone.now)
	title = models.CharField(max_length=30)
	readCnt = models.IntegerField()
	tags = models.ForeignKey(Tags)
	user = models.ForeignKey(Users)

	def __unicode__(self):
		return "%s   %s" % (self.title, self.time)

class Comment(models.Model):
	article = models.ForeignKey(Article)
	isParent = models.BooleanField(default=False)
	time = models.DateField(default=timezone.now)
	content = models.CharField(max_length=30, default="")

	def __unicode__(self):
		return "%s   %s" % (self.content[:10], self.time)