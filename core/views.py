from django.shortcuts import render, redirect
from classroom.models import ClassRoom, ClassRoomJoined
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'core/index.html')

    if request.user.info.account_type =='student':
        data = ClassRoomJoined.objects.filter(user = request.user)
        print(data)
        return render(request, 'core/index.html', {'data':data})

    if request.user.info.account_type =='teacher':
        data = ClassRoom.objects.filter(user = request.user)
        return render(request, 'core/index.html', {'data':data})


    return render(request, 'core/index.html')