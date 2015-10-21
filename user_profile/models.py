from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.

class UserProfile(models.Model):
	social_id = models.TextField(default="")
	social_alias = models.TextField(default="")
	social_first_name = models.TextField(default="")
	social_last_name = models.TextField(default="")
	social_email = models.TextField(default="", unique = True)
	social_gender = models.TextField(default="")
	social_language = models.TextField(default="")
	social_avatar = models.TextField(default="")
	def __unicode__(self):
		return self.social_id