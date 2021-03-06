from django.db import models

# Create your models here.
import os, random, string
from slugify import slugify
import django.contrib.auth.hashers as hashers

from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }






from django.db import models
import os, random, string
from slugify import slugify
import django.contrib.auth.hashers as hashers

def random_name():
    name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return name


class Profile(models.Model):
    user = models.OneToOneField(User, to_field='id', on_delete=models.CASCADE,null = True)
    gender = models.CharField(max_length=2, choices=
        (('M', 'Male'),
         ('F', 'Female'),
         ('O', 'Others'),
        ),null = True)
    slug = models.SlugField(unique=True, max_length=50, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_picture/'+random_name(),null = True)

    def __str__(self):
        return self.slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        hapazat = self.user.username
        slug = slugify(hapazat)
        if self.slug != slug:
            self.slug = slug
        return super(Profile, self).save()