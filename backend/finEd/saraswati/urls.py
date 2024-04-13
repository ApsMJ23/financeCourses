from django.urls import path
from . import views

urlpatterns = [
    path('userCourses/', views.userCources, name='userCourses'),
    path('updateUserCourse/', views.updateUserCourse, name='updateUserCourse')
]