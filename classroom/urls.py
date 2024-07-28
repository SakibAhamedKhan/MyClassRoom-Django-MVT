from django.urls import path, include
from  . import views
urlpatterns = [
    path('createclassroom/', views.createClassRoom,name='createClassRoom' ),
    path('classroompage/<int:id>', views.classRoomPage,name='classRoomPage' ),
    path('classroompage/addpost/<int:classRoomId>', views.classRoomAddPost,name='classRoomPage/addpost' ),
    path('classroompage/updateclassroom/<int:classRoomId>', views.updateClassRoom,name='classRoomPage/updateclassroom' ),
    path('classroompage/managestudent/<int:classRoomId>', views.manageClassRoomStudent,name='classroompage/managestudent/' ),
    path('classroompage/managestudent/remove/<int:id>/<int:classRoomId>', views.removeStudentFromRoom,name='classroompage/managestudent/remove' ),
    path('classjoin/', views.classJoin, name='classJoin'),
]
