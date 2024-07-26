from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClassRoomForm, ClassRoomPostForm
from .models import ClassRoom, ClassRoomPost, ClassRoomJoined
# Create your views here.
def createClassRoom(request):
    if request.user.info.account_type =='student':
        messages.success(request, 'You are not allowed to create classroom!')
        return redirect('index')

    if request.method == 'POST':
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Classroom is created successfull!')
            subject = form.cleaned_data.get('subject')
            classroom_name = form.cleaned_data.get('classroom_name')
            invitation_code = form.cleaned_data.get('invitation_code')
            ClassRoom.objects.create(
                user = request.user,
                subject = subject, 
                classroom_name = classroom_name,
                invitation_code = invitation_code
            )
            return redirect('index')
    else :
        form = ClassRoomForm()
    return render(request, 'classroom/createClassRoom.html', {'form':form})

def updateClassRoom(request, classRoomId):
    if request.user.info.account_type =='student':
        messages.success(request, 'You are not allowed to add post on classroom!')
        return redirect('index')
    
    specific_room = ClassRoom.objects.get(id=classRoomId)
    if specific_room.user!=request.user:
        messages.success(request, 'You are not allowed to post in this classroom')
        return redirect('classRoomPage',classRoomId)
    
    form = ClassRoomForm(instance=specific_room)

    if request.method == 'POST':
        form = ClassRoomForm(request.POST, instance=specific_room)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classroom updated successfully!')
            return redirect('classRoomPage',classRoomId)
        
    return render(request, 'classroom/teacher/classUpdate.html', {'form':form, 'room_data':specific_room})


def classRoomPage(request, id):
    specific_room = ClassRoom.objects.get(id=id)
    if specific_room.user!=request.user:
        messages.success(request, 'You are not allowed to enter this classroom')
        return redirect('index')
    
    specific_room_post = ClassRoomPost.objects.filter(classroom=specific_room)
    return render(request, 'classroom/classRoomPage.html',{'data':specific_room, 'post_data':specific_room_post})



def classRoomAddPost(request, classRoomId):
    # return redirect('classRoomPage',classRoomId)
    if request.user.info.account_type =='student':
        messages.success(request, 'You are not allowed to add post on classroom!')
        return redirect('index')
    
    specific_room = ClassRoom.objects.get(id=classRoomId)
    if specific_room.user!=request.user:
        messages.success(request, 'You are not allowed to post in this classroom')
        return redirect('classRoomPage',classRoomId)
    
    if request.method == 'POST':
        form = ClassRoomPostForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Classroom post added successfully!')
            description = form.cleaned_data.get('description')
            title = form.cleaned_data.get('title')
            ClassRoomPost.objects.create(
                user = request.user, 
                classroom = specific_room,
                description = description,
                title = title,
            )
            return redirect('classRoomPage',classRoomId)
        
    else :
        form = ClassRoomPostForm()
    
    return render(request, 'classroom/teacher/addpost.html', {'form':form, 'room_data':specific_room})


def manageClassRoomStudent(request, classRoomId):
    if request.user.info.account_type =='student':
        messages.success(request, 'You are not allowed to add post on classroom!')
        return redirect('index')
    
    specific_room = ClassRoom.objects.get(id=classRoomId)
    if specific_room.user!=request.user:
        messages.success(request, 'You are not allowed to post in this classroom')
        return redirect('classRoomPage',classRoomId)
    
    classroom_joined = ClassRoomJoined.objects.filter(classroom=specific_room)

    return render(request, 'classroom/teacher/manageStudent.html', {'room_data':specific_room, 'classroom_joined':classroom_joined})
    

def removeStudentFromRoom(request, id, classRoomId):
    if request.user.info.account_type =='student':
        messages.success(request, 'You are not allowed to add post on classroom!')
        return redirect('index')
    
    specific_room = ClassRoom.objects.get(id=classRoomId)
    if specific_room.user!=request.user:
        return redirect('classRoomPage',classRoomId)
        messages.success(request, 'You are not allowed to post in this classroom')
    student = ClassRoomJoined.objects.get(id = id)
    messages.success(request, f"{student.user.first_name} {student.user.last_name} removed successfully")
    student.delete()
    return redirect('classroompage/managestudent/',classRoomId)
    