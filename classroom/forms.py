from django import forms
from .models import ClassRoom, ClassRoomPost
class ClassRoomForm(forms.ModelForm):
    class Meta:
        model = ClassRoom
        exclude =['user']


class ClassRoomPostForm(forms.ModelForm):
    class Meta:
        model = ClassRoomPost
        exclude = ['user', 'classroom']
