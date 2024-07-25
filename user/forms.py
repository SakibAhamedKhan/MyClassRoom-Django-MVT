from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import ROLE_TYPE, GENDER_TYPE
from django.contrib.auth.models import User
from .models import UserExtraInfo

class UserExtraInfoForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=ROLE_TYPE)
    institute = forms.CharField(max_length=30)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date', 'gender', 'institute']

    def save(self, commit=True):
        me = super().save(commit=False)
        if commit == True:
            me.save()
            account_type = self.cleaned_data.get('account_type')
            institute = self.cleaned_data.get('institute')
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            iSTeacher = False
            if account_type=='teacher':
                iSTeacher = True
            UserExtraInfo.objects.create(
                user = me, 
                account_type = account_type,
                institute = institute,
                birth_date = birth_date,
                gender = gender,
                roll_no = 10000+me.id,
                iSTeacher =iSTeacher,
            )

        return me

class UserUpdateForm(forms.ModelForm):
    institute = forms.CharField(max_length=100)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance:
            try:
                user_info = self.instance.info
            except UserExtraInfo.DoesNotExist:
                user_info = None

            if user_info:
                self.fields['institute'].initial = user_info.institute
                self.fields['birth_date'].initial = user_info.birth_date
                self.fields['gender'].initial = user_info.gender

    def save(self, commit=True):
        me = super().save(commit=False)
        if commit == True:
            me.save()

            user_info = UserExtraInfo.objects.get(user=me)

            user_info.institute = self.cleaned_data.get('institute')
            user_info.birth_date = self.cleaned_data.get('birth_date')
            user_info.gender = self.cleaned_data.get('gender')
            user_info.save()

        return me