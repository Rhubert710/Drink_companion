from django.db import models
from django.conf import settings




class LikedDrink (models.Model):

    drinkId = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    liked = models.BooleanField()

class Comment (models.Model):
    
    drinkId = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    text = models.CharField(max_length=401)
