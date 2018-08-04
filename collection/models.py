from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    category_title = models.CharField(max_length=100)
    category_use = models.CharField(max_length=100)
    category_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.category_title + ' - '+self.category_use


class dresses(models.Model):
    dress_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    dress_title = models.CharField(max_length=100)
    dress_price = models.IntegerField()
    dress_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.dress_title


class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.user_name


