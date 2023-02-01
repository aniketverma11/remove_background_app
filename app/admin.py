from django.contrib import admin

# Register your models here.
from .models import Image, Result

admin.site.register(Image)
admin.site.register(Result)