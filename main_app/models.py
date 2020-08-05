from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.dispatch import receiver

# # Create your models here.


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

    @reciever(post_save, sender=User)
    def create_user_profile(sender, instance, created):
        if created:
            Profile.objects.create(user=instance)

    @reciever(post_save, sender=User)
    def save_user_profile(sender, instance):
        instance.profile.save()


class Post(models.Model):
    author = models.ForeignKey(custom_user, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
