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
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('createAccount/', views.createAccount, name='createAccount'),
    

    # path('<slug>', views.index, name='index'),
    
]