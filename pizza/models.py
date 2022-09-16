from django.db import models

from django.contrib.auth.models import User


class Pizzeria(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=40)


class Pizza(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
    thumbnail_url = models.URLField(default=None, blank=True, null=True)
    approved = models.BooleanField(default=False)
    creator = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
