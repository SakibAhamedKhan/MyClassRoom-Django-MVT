from django.db import models
from django.contrib.auth.models import User
from .constants import ROLE_TYPE, GENDER_TYPE
# Create your models here.
class UserExtraInfo(models.Model):
    user = models.OneToOneField(User, related_name='info', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20, choices=ROLE_TYPE)
    iSTeacher = models.BooleanField(default=False)
    institute = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    roll_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.roll_no)
    


    