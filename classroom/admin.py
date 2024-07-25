from django.contrib import admin
from .models import ClassRoom, ClassRoomJoined, ClassRoomPost
# Register your models here.

admin.site.register(ClassRoom)
admin.site.register(ClassRoomJoined)
admin.site.register(ClassRoomPost)
