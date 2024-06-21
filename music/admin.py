from django.contrib import admin

# Register your models here.
from .models import Singer, Album, Song

admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(Song)
