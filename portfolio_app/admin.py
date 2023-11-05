from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

# Register your models here so they can be edited in admin panel
admin.site.register(Musician)
admin.site.register(Piece)