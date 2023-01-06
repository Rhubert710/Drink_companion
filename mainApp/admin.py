from django.contrib import admin
from mainApp.models import *

admin.site.register(LikedDrink)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)



# Register your models here.
