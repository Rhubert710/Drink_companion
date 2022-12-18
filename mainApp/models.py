from django.db import models
from django.conf import settings

from django.contrib.auth.models import User



class userAccount (models.Model):
    
    username = models.CharField(max_length=17)
    password = models.CharField(max_length=17)
    

class LikedDrink (models.Model):

    drinkId = models.CharField(max_length=200)
    user = models.ForeignKey ( User , on_delete=models.CASCADE )

    liked = models.CharField( max_length=7 ) #' true' or 'false'




class Comment (models.Model):
    
    drinkId = models.CharField(max_length=200)
    user = models.ForeignKey ( User , on_delete=models.CASCADE )
    text = models.CharField(max_length=401)
    pub_date = models.DateTimeField(auto_now_add=True)





    


