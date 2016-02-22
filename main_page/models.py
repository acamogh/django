from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Signup(models.Model):
    email = models.EmailField(max_length=128)
    fullname = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.email