from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from core.models import MyUser
# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    ordering=['id']
    list_display=['email','name']
admin.site.register(models.MyUser,MyUserAdmin)

