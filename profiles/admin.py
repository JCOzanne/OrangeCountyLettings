from linecache import clearcache

from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

