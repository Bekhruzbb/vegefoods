from django.contrib import admin
from .models import Favorite, UserCustomUser
# Register your models here.
admin.site.register([Favorite, UserCustomUser])