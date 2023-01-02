from django.urls import path
from . import views

from django.contrib import admin

urlpatterns = [

    path('', views.index, name='index'),
    path('drink', views.index, name='drinkPage'),
    path('browse', views.index, name='browse'),
    path('profilePage', views.index, name='profilePage'),
    path('likeDrink/', views.likeDrink, name='likeDrink'),
    path('postComment/', views.postComment, name='postComment'),
    path('getComments', views.getComments, name='getComments'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('test/', views.test, name='test'),
    path('createAccount/', views.createAccount, name='createAccount'),
    
]




handler404 = handler500 = 'mainApp.views.index'