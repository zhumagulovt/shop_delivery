from django.db import models
from django.contrib.auth import get_user_model


class Courier(models.Model):
	
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)


class Order(models.Model):

	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	completed = models.BooleanField(default=False)
