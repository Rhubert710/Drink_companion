from django.contrib import admin
from mainApp.models import *

# admin.site.register(Test)
admin.site.register(LikedDrink)
admin.site.register(Comment)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    readonly_fields = ('pub_date',)
# Register your models here.
