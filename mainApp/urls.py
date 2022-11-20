from django.urls import path
from . import views

from django.contrib import admin

urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('<slug>', views.index, name='index'),
    
]