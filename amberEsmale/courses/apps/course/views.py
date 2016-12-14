from django.shortcuts import render, redirect
from .models import Course
from ..course.models import User
from django.db import models

# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all(),
        'all_users' : User.objects.all()
    }
    return render(request, 'course/index.html', context)

def add_course(request):
    Course.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def add_user(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect('/')
def remove_course(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')

def add_users_courses(request):
    # added_user = User.objects.filter(name = request.POST['user'])
    # User.Course.add(name = request.POST['course'])
    context = {
        'all_users' : User.objects.all(),
        'all_courses' : Course.objects.all()
    }
    return render(request, 'course/users_courses.html', context)

def enroll(request):
    course = Course.objects.get(id = request.POST['course'])
    user = User.objects.get(id = request.POST['user'])
    course.users.add(user)
    return redirect('/users_course')
