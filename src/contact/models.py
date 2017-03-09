from __future__ import unicode_literals

from django.db import models

# Create your models here.
class contact(models.Model):
	name = models.CharField(max_length=120)
	email = models.CharField(max_length=100)
	telp = models.CharField(max_length=100, default='+62')
	deskripsi = models.TextField(max_length=120, blank=True, null=True)
	#location = models.CharField(max_length=120, default='my location default', blank=True, null=True)
	#job = models.CharField(max_length=120, null=True)


	def __unicode__(self):
		return self.name