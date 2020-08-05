from django.db import models
from datetime import date
from django.contrib.auth.models import User

# # Create your models here.


# City Model


class City(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    # image = models.ImageField(upload_to="images/")#


# Django model username, email, password, first_name, and last_name
# User Model
class User_ext(models.Model):
    email = models.EmailField(("email password"), unique=True)
    locaton = models.CharField(max_length=40)
    # photos = models.ImageField(upload_to="images/user_photos")
    date_created = models.DateTimeField()

    def __str__(self):
        return f"{self.email}, {self.username}, {self.first_name}"


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
