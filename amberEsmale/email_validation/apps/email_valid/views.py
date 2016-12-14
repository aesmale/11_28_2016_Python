from django.shortcuts import render, redirect, HttpResponse
from .models import EmailManager, Email
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def index(request):
    return render(request, 'email_valid/index.html')

# def success(request):
#     context = {
#         Email.objects.all()
#     }
#     return render(request, 'email_valid/success.html', context)

def add_email(request):
    try:
        email = request.POST['email']
        if Email.objects.validate(email) == True:
            Email.objects.create(email=email)
            request.session['email'] = email
            context = {
                'emails' : Email.objects.all()
            }
            return render(request, 'email_valid/success.html', context)
        else:
            messages.add_message(request, messages.SUCCESS, 'This is not a valid email!')
            print "This is not a valid email!"
            return redirect('/')
    except MultiValueDictKeyError:
            request.session.flush()
            context = {
                'emails' : Email.objects.all()
            }
            return render(request, 'email_valid/success.html', context)
