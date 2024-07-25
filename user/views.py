from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserExtraInfoForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserExtraInfoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save();
            return redirect('index')
    else:
        form = UserExtraInfoForm()
    return render(request, 'user/register.html', {'form':form})

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']

                user = authenticate(username = name, password = userpass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successfully')
                    return redirect('profile')
        else :
            form = AuthenticationForm();
        return render(request, 'user/login.html', {'form':form})
    else:
        return redirect('profile')
    
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')


    if request.method=='GET':
        form = UserUpdateForm(instance=request.user)
        return render(request, 'user/profile.html', {'form':form})
    if request.method=='POST':
        form = UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            return redirect('profile')



def userLogout(request):
    logout(request)
    return redirect('login')



def passChange(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password changed successfully')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'user/passchange.html', {'form': form})
    else:
        return redirect('login')