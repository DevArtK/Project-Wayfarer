from django.contrib import admin
from .models import City, User_ext, Post

# Register your models here.

admin.site.register(City)
admin.site.register(Post)
admin.site.register(User_ext)