from django.contrib import admin
from .models import *
from taggit.models import Tag
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
