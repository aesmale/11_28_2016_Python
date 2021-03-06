from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
