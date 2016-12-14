from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re, bcrypt
import hashlib, sys
from django.contrib.auth.hashers import check_password
password = b"super secret password"

# Create your models here.
class UserManager(models.Manager):
    def valid_name(self, request, name, type):
        if len(name) < 2 or not re.match(r'^[a-zA-Z]+$', name):
            messages.add_message(request, messages.INFO, 'Your ' +type+ ' name must be longer than 2 characters and may only contain letters', extra_tags="register")
            print "somethindsnivndsiovcfisovfijcsviofmvlvjiols"
        if len(name) < 2 or not re.match(r'^[a-zA-Z]+$', name):
            return False
        else:
            return True

    def valid_email(self, request, email):
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
            messages.add_message(request, messages.INFO, 'invalid email', extra_tags="register")
            return False
        if User.objects.filter(email=email):
            messages.add_message(request, messages.INFO, 'email already exists in database..', extra_tags="register")
            return False
        return True
    def valid_password(self, request, password):
        if len(password) < 8:
            messages.add_message(request, messages.INFO, 'invalid password', extra_tags="register")
            return False
        else:
            return True


class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    pass
