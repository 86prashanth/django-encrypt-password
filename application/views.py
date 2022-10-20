from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models import Login,Emplogin
from .encrypt_util import *
# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print('Original Password:', request.POST['password'])
        encryptpass= encrypt(request.POST['password'])
        print('Encrypt Password:',encryptpass)
        decryptpass= decrypt(encryptpass)
        print('Decrypt Password:',decryptpass)
        data=Emplogin(name=name, email=email, password=password)
        data.save()
        return HttpResponse('Done')
    else:
        return render(request, 'app/index.html')
    
    
