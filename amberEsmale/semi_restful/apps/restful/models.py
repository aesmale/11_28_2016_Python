from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500)
    price = models.DecimalField(max_digits = 50, decimal_places= 2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
