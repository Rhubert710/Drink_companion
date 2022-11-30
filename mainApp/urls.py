from django.urls import path
from . import views

from django.contrib import admin

urlpatterns = [

    path('', views.index, name='index'),
    path('drink', views.index, name='drinkPage'),
    path('browse', views.index, name='browse'),
    path('likeDrink/', views.likeDrink, name='likeDrink'),
    path('login/', views.login, name='login'),
    path('createAccount/', views.createAccount, name='createAccount'),
    

    # path('<slug>', views.index, name='index'),
    
]