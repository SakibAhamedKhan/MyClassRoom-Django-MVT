from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClassRoom(models.Model):
    user = models.ForeignKey(User, related_name='classR', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    classroom_name = models.CharField(max_length=100)
    invitation_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.classroom_name

class ClassRoomJoined(models.Model):
    user = models.ForeignKey(User, related_name='classRJ', on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.classroom.classroom_name

class ClassRoomPost(models.Model):
    user = models.ForeignKey(User, related_name='classRP', on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    


