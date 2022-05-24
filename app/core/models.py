from typing import Optional, Union
from django.db import models
from django.contrib.auth import get_user_model
from .helpers.models import TrackingModel
from django.contrib.auth.models import (PermissionsMixin,BaseUserManager,AbstractBaseUser,UserManager)
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator

#add new properties access token, email verified
# use email and password instead of username/password


class MyUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        
        if not username:
            raise ValueError('Username must be set')
        if not email:
            raise ValueError('Email must be set')
        
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    
    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    username_validator: UnicodeUsernameValidator()

    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=False, unique=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()
    email_verified = models.BooleanField(default=False)

    objects: MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    @property
    def token(self):
        pass
