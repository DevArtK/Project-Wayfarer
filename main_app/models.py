from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User, PermissionsMixin
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.base_user import BaseUserManager
# class UserManager(BaseUserManager):

#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         '''Create and save a user with the given email, and
#         password.
#         '''
#         if not email:
#             raise ValueError('The given email must be set')

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must have is_staff=True.'
#             )
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must have is_superuser=True.'
#             )

#         return self._create_user(email, password, **extra_fields)

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
        instance.User.save()

    def __str__(self):
        return self.User.username


# User Manager Defines what happens when a regular, and super user is created

# City Model

STATES = (
    (USA, 'USA'),
    (Alabama_Montgomery, 'Alabama, Montgomery'),
    (Alaska_Juneau, 'Alaska, Juneau'),
    (Arizona_Phoenix, 'Arizona, Phoenix'),
    (Arkansas_Little Rock, 'Arkansas, Little Rock'),
    (California_Sacramento, 'California, Sacramento'),
    (Colorado_Denver, 'Colorado, Denver'),
    (Connecticut_Hartford, 'Connecticut, Hartford'),
    (Delaware_Dover, 'Delaware, Dover'),
    (Florida_Tallahassee, 'Florida, Tallahassee'),
    (Georgia_Atlanta, 'Georgia, Atlanta'),
    (Hawaii_Honolulu, 'Hawaii, Honolulu'),
    (Idaho_Boise, 'Idaho, Boise'),
    (Illinois_Springfield, 'Illinois, Springfield'),
    (Indiana_Indianapolis, 'Indiana, Indianapolis'),
    (Iowa_Des Moines, 'Iowa, Des Moines'),
    (Kansas_Topeka, 'Kansas, Topeka'),
    (Kentucky_Frankfort, 'Kentucky, Frankfort'),
    (Louisiana_Baton Rouge, 'Louisiana, Baton Rouge'),
    (Maine_Augusta, 'Maine, Augusta'),
    (Maryland_Annapolis, 'Maryland, Annapolis'),
    (Massachusetts_Boston, 'Massachusetts, Boston'),
    (Michigan_Lansing, 'Michigan, Lansing'),
    (Minnesota_St_Paul, 'Minnesota, St. Paul'),
    (Mississippi_Jackson, 'Mississippi, Jackson'),
    (Missouri_Jefferson City, 'Missouri, Jefferson City'),
    (Montana_Helena, 'Montana, Helena'),
    (Nebraska_Lincoln, 'Nebraska, Lincoln'),
    (Nevada_Carson City, 'Nevada, Carson City'),
    (New Hampshire_Concord, 'New Hampshire, Concord'),
    (New Jersey_Trenton, 'New Jersey, Trenton'),
    (New Mexico_Santa Fe, 'New Mexico, Santa Fe'),
    (New York_Albany, 'New York, Albany'),
    (North Carolina_Raleigh, 'North Carolina, Raleigh'),
    (North Dakota_Bismarck, 'North Dakota, Bismarck'),
    (Ohio_Columbus, 'Ohio, Columbus'),
    (Oklahoma_Oklahoma City Oklahoma, 'Oklahoma City'),
    (Oregon_Salem Portland Oregon, 'Salem Portland'),
    (Pennsylvania_Harrisburg, 'Pennsylvania, Harrisburg'),
    (Rhode Island_Providence, 'Rhode Island, Providence'),
    (South Carolina_Columbia, 'South Carolina, Columbia'),
    (South Dakota_Pierre, 'South Dakota, Pierre'),
    (Tennessee_Nashville, 'Tennessee, Nashville'),
    (Texas_Austin, 'Texas, Austin'),
    (Utah_Salt Lake City, 'Utah, Salt Lake City'),
    (Vermont_Montpelier, 'Vermont, Montpelier'),
    (Virginia_Richmond, 'Virginia, Richmond'),
    (Washington_Olympia, 'Washington, Olympi'a),
    (West Virginia_Charleston, 'West Virginia, Charleston'),
    (Wisconsin_Madison, 'Wisconsin, Madison'),
    (Wyoming_Cheyenne, 'Wyoming, Cheyenne'),
)


class City(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(
        'Current Location', max_length=1, choices=STATES, default=STATES[0])
    image = models.ImageField(upload_to="images/")


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
