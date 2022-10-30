from django.shortcuts import render
from mainApp.templates.mainApp import *


def index (request):

    return render(request, 'mainApp/index.html')