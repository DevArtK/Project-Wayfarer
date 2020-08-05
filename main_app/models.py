from django.db import models

# # Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    display_name = models.Charfield(max_length=30)
    # password =
    email = models.EmailField(("email password"), unique=True)
    locaton = models.CharField(max_length=40)
    # first_name =
    # last_name =
    photos = models.ImageField(upload_to="images/user_photos")
    date_created = models.DateTimeField()

    def __str__(self):
        return f"{self.email}, {self.username}, {self.first_name}"

