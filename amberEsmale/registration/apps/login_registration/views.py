from django.shortcuts import render, redirect, HttpResponse
from .models import UserManager, User
from django.contrib import messages
import bcrypt
import hashlib, sys
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def register(request):
    valid_first = User.objects.valid_name(request, request.POST['first_name'], "first")
    valid_last = User.objects.valid_name(request, request.POST['last_name'], "last")
    valid_password = User.objects.valid_password(request, request.POST['password'])
    valid_email = User.objects.valid_email(request, request.POST['email'])
    if request.POST['password'] != request.POST['confirm']:
        messages.add_message(request, messages.INFO, 'Your passwords must match', extra_tags = "register")
    if valid_email == True and valid_first == True and valid_last == True and valid_password == True:
        salt = bcrypt.gensalt()
        password = request.POST['password']
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = bcrypt.hashpw(password.encode('utf-8'), salt))
        print "succes!!!"
        if 'first_name' in request.session:
            request.session.flush()
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        context = {
            'method' : 'registering!'
        }
        return render(request, 'login_registration/success.html', context)
    else:
        return redirect('/')


def login(request):
    try:
        email = request.POST['email']
        password = request.POST['password'].encode('utf-8')
        user = User.objects.filter(email = email)
        hashed = user[0].password.encode('utf-8')
        if bcrypt.hashpw(password, hashed) == hashed:
            context = {
                'method' : "logging in!"
            }
            if 'first_name' in request.session:
                request.session.flush()
            request.session['first_name'] = user[0].first_name
            request.session['last_name'] = user[0].last_name
            request.session['email'] = user[0].email
            return render(request, "login_registration/success.html", context)
        else:
            messages.add_message(request, messages.INFO, 'invalid username/password', extra_tags = 'login')
    except (User.DoesNotExist, ValueError, IndexError):
        messages.add_message(request, messages.INFO, 'invalid username/password', extra_tags = 'login')
        return redirect('/')
