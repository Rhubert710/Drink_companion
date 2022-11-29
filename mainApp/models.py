from django.db import models
from django.conf import settings





class userAccount (models.Model):
    
    username = models.CharField(max_length=17)
    password = models.CharField(max_length=17)
    

class LikedDrink (models.Model):

    drinkId = models.CharField(max_length=200)
    user = models.ForeignKey ( userAccount , on_delete=models.CASCADE )

    liked = models.BooleanField()




class Comment (models.Model):
    
    drinkId = models.CharField(max_length=200)
    user = models.ForeignKey ( userAccount , on_delete=models.CASCADE )

    text = models.CharField(max_length=401)





    


