import os
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def callback(request):
    subject = "Test Email"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = "cbkurltest@mailinator.com"
    message = "Prova di invio della mail da Django"

    send_mail(subject=subject, 
    from_email=from_email, 
    recipient_list=[to_email],
    message=message, 
    fail_silently=False)#Change to true



    return HttpResponse("Test")
