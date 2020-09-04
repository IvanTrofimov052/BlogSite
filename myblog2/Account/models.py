from django.db import models


class Login(models.Model):
	user_name = models.CharField(max_length=20)
	user_password = models.CharField(max_length=65)


class Session(models.Model):
	user_name = models.CharField(max_length=20)
	session = models.CharField(max_length=65)