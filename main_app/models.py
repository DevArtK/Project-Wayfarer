from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User, PermissionsMixin
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class UserProfile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    # Required
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=128, verbose_name="password")
    email = models.EmailField(unique=True, verbose_name="Email", max_length=60)
    date_joined = models.DateTimeField(
        verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    first_name = models.CharField(
        verbose_name="First Name", max_length=50, blank=True)
    last_name = models.CharField(
        verbose_name="Last Name", max_length=50, blank=True)
    location = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User.objects.create(user=instance).save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user.save()

    def __str__(self):
        return self.user.username


# User Manager Defines what happens when a regular, and super user is created

# City Model


class City(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    # image = models.ImageField(upload_to="images/")#


# Django model username, email, password, first_name, and last_name
# User Model
class custom_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    locaton = models.CharField(max_length=40)
    email = models.EmailField(("email address"), unique=True)
    first_name = models.CharField(("first name"), max_length=30, blank=True)
    last_name = models.CharField(("last name"), max_length=30, blank=True)
    date_joined = models.DateTimeField(("date joined"), auto_now_add=True)
    is_active = models.BooleanField(("active"), default=True)
    date_created = models.DateTimeField()
    # photos = models.ImageField(upload_to="images/user_photos")

    def __str__(self):
        return f"{self.email}, {self.username}, {self.first_name}"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
