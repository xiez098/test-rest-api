from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin,UserManager
# BaseUserManager provides helper function for creating user

class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        """create and save user"""
        if not email:
            print("invalide user email")
            raise ValueError
        user=self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        user=self.create_user(email,password)
        user.is_staff =True
        user.is_superuser=True
        user.save(using=self._db)
        return user
    

class MyUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    objects=MyUserManager()
    USERNAME_FIELD='email'
