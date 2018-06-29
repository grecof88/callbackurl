import os
import requests
import json
from requests.auth import HTTPBasicAuth
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import LogForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        subject = "Callback"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = "cbkurltest@mailinator.com"
        body_unicode = request.body.decode('utf-8')
        #body = json.loads(body_unicode)
        
        message = body_unicode#json.dumps(body)

        send_mail(subject=subject, 
        from_email=from_email, 
        recipient_list=[to_email],
        message=message, 
        fail_silently=False)#Change to true
        return HttpResponse("OK")
    else:
        return HttpResponse("KO")
    #    form = LogForm()
    #    return render(request, 'cbkform.html', {'form': form})


def setcbk(request):
    if request.method == 'POST':
        #form = LogForm(request.POST)
        
        headers = {'content-type':'application/json'}
        payload = {'url': 'http://cbu-callbackurl.1d35.starter-us-east-1.openshiftapps.com/callback'}
        url = request.POST['api_url']
        user = request.POST['username']
        pwd = request.POST['password']

        r = requests.post(url, json=payload, auth=HTTPBasicAuth(user,pwd), headers=headers)

        return HttpResponse(r)
    else:
        return HttpResponse("Fail")
