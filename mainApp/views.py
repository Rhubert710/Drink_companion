from django.shortcuts import render
from mainApp.templates.mainApp import *

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.http import JsonResponse
import ast


def index (request, slug=''):
    return render(request, 'mainApp/index.html')

def createUser(request):
    print(request.POST)
    # user = authenticate(username=request.POST.username, password=request.POST.password)
    # if user is not None:
    #     return JsonResponse({message:'That username aready exists'})
   
    # else:
    #     user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


def login (request):
    
    body = ast.literal_eval(request.body.decode('"UTF-8"'))
    
    print( body['username'] )
    return JsonResponse({'message':'That username aready exists'})
