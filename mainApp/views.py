from django.shortcuts import render , redirect
from mainApp.templates.mainApp import *

from django.contrib.auth import authenticate , logout as auth_logout , login as auth_login
from django.contrib.auth.models import User
from mainApp.models import *
from django.http import JsonResponse , HttpResponse
import ast
import json
from django.template.loader import render_to_string
from mainApp.forms import *


def index (request, slug=''):

    if request.user.is_authenticated:

        likedList , dislikedList = get_liked_lists(request.user)
        return render(request, 'mainApp/index.html' , { 'liked':likedList , 'disliked':dislikedList , 'user': request.user } )
    
    
    
    
    else:
        return render(request, 'mainApp/index.html')






def likeDrink (request):

    body = json.loads(request.body.decode('utf-8'))
    
    # check or existing objefts
    existing_ob = LikedDrink.objects.filter( user=request.user , drinkId=body['drinkId'])
    
    if existing_ob:

        if existing_ob.filter(liked=body['liked']):

            existing_ob.delete()
            return JsonResponse({'status':'200' , 'message':'item deleted'}) # delete
        
        else:

            existing_ob.update( liked=body['liked'] )
            return JsonResponse({'status':'200' , 'message':'item updated'}) # update
    
    else:

        LikedDrink( user=request.user , drinkId=body['drinkId'] , liked=body['liked']).save()
        return JsonResponse({'status':'200' , 'message':'item created'}) # create



def postComment(request):

    form = CommentForm ( request.POST )

    if form.is_valid():
        form.save()

    comments = Comment.objects.filter( drinkId= request.POST['drinkId'] )

    redered_commentsList = render_to_string( 'mainApp/commentsList.html' , { 'comments' : comments } )
    return JsonResponse ( { 'commentList_HTML' : redered_commentsList } )


def createAccount(request):
    
    # body as dict ()
    body = ast.literal_eval(request.body.decode('"UTF-8"'))

    user = authenticate( request, username=body['username'], password=body['password'] )
    
    if user is None:
        
        user = User.objects.create_user( username=body['username'], password=body['password'] )
        auth_login(request, user)

        return JsonResponse({
            'successful' : 'true',
            'message' : 'Welcome',
            'username' : user.get_username(),
            'session' : user.get_session_auth_hash(),
            })

    else:
        return JsonResponse({
            'successful' : 'false',
            'message' : 'An account with that username already exists',
            })



def login (request):
    
    # body as dict ()
    body = ast.literal_eval(request.body.decode('"UTF-8"'))

    user = user = authenticate( request, username=body['username'], password=body['password'] )

    if user is not None:

        auth_login(request, user)
        
        likedList , dislikedList = get_liked_lists ( user )

        return JsonResponse({
            'successful' : 'true',
            'message' : 'Welcome Back',
            'username' : user.get_username(),
            'session' : user.get_session_auth_hash(),
            'likedDrinks' : likedList,
            'dislikedDrinks' : dislikedList,
            })

    else:
        return JsonResponse({
            'successful' : 'false',
            'message' : 'user doesnt exist',
            })




def logout ( request ):

    auth_logout(request)
    return redirect ( 'index' ) #add success modal


""" non-path functions"""
def get_liked_lists ( user ):
    
    likedList = list(LikedDrink.objects.filter( user=user, liked='true').values_list('drinkId', flat=True))
    dislikedList = list(LikedDrink.objects.filter(user=user, liked='false').values_list('drinkId', flat=True))

    return likedList, dislikedList