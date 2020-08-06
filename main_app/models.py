from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         ProfileForm.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.ProfileForm.save()

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

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
    def create_user_profile(sender, instance, created):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance):
        instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


# class User_Profile_Manager(BaseUserManager):
#     def create_user(self, email, username, password=None, is_staff=False, is_admin=False, is_active=False):  # Same As Required Fields
#         if not email:
#             raise ValueError("Users must have an email-address")
#         if not username:
#             raise ValueError("Users must have a username")

#         user = self.model(email=self.normalize_email(email),
#                           username=username)
#         user.staff = staff
#         user.admin = admin
#         user.active = active
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_superuser(self, email, username, password, **extra_fields):
#         if not email:
#             raise ValueError("Users must have an email-address")
#         if not username:
#             raise ValueError("Users must have a username")

#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password)
#         user.username = username,
#         user.staff = True,
#         user.active = True,
#         user.admin = True,
#         user.save(using=self.db)
#         return user


# # Django model username, email, password, first_name, and last_name
# # User Model
# class User_Profile(models.Model):
#     User = models.OneToOneField(User, on_delete=models.CASCADE)
#     id = models.AutoField(primary_key=True)
#     # Required
#     username = models.CharField(unique=True, max_length=50)
#     password = models.CharField(max_length=128, verbose_name="password")
#     email = models.EmailField(
#         unique=True, verbose_name="Email", max_length=60)
#     date_joined = models.DateTimeField(
#         verbose_name="Date Joined", auto_now_add=True)
#     last_login = models.DateTimeField(
#         verbose_name="Last Login", auto_now=True)
#     active = models.BooleanField(default=False)
#     staff = models.BooleanField(default=False)
#     superuser = models.BooleanField(default=False)
#     location = models.CharField(max_length=50)
#     first_name = models.CharField(
#         verbose_name="First Name", max_length=50, blank=True)
#     last_name = models.CharField(
#         verbose_name="Last Name", max_length=50, blank=True)
#     picture = models.ImageField(blank=True, null=True)

#     USERNAME_FIELD = "username"  # What they log in with
#     REQUIRED_FIELDS = ["email", "password"]  # When registering
#     # photos = models.ImageField(upload_to="images/user_photos")

#     objects = User_Profile_Manager()

#     def __str__(self):
#         if self.first_name is not None:
#             return self.username()
#         return self.email

#     def get_full_name(self):
#         return f"{self.first_name}, {self.last_name}"

#     def short_name(self):
#         return self.first_name

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     # !
#     def is_staff(self):
#         return self.is_staff

#     def is_admin(self):
#         return self.is_admin

#     # !
#     def is_active(self):
#         return self.is_active

#     def is_superuser(self):
#         return self.is_admin
