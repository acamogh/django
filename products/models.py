from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    active = models.BooleanField(default=True)


    def __unicode__(self): #def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Product_Detail',kwargs={'pk':self.pk})