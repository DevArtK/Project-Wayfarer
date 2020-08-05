from django.contrib import admin
from .models import City, custom_user, Post

# Register your models here.

admin.site.register(City)
admin.site.register(Post)
admin.site.register(custom_user)
