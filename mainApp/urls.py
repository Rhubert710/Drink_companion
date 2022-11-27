from django.urls import path
from . import views

from django.contrib import admin

urlpatterns = [

    path('', views.index, name='index'),
    path('drink', views.index, name='drinkPage'),
    path('browse', views.index, name='browse'),
    path('createUser/', views.createUser, name='createUser'),
    

    # path('<slug>', views.index, name='index'),
    
]