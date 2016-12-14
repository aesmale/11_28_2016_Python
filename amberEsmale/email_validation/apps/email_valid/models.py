from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
class EmailManager(models.Manager):
    def validate(self, email):
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
            return False
        else:
            return True

class Email(models.Model):
    email = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EmailManager()
