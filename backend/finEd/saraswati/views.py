from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .models import UserCourse
from rest_framework import status
from .serializers import UserCourseSerializer
from datetime import datetime
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def userCources(request):
    user = request.data['userId']
    userCourses = UserCourse.objects.filter(userId=user)
    if userCourses:
        course = UserCourseSerializer(userCourses,many=True)
        return Response({'userCourses': course.data }, status=status.HTTP_200_OK)
    else:
        UserCourse.objects.create(userId=user,isCourseStarted=False,courseId=1,startDate='2020-01-01',endDate='2020-01-01')
        userCourses = UserCourse.objects.filter(userId=user)
        course = UserCourseSerializer(userCourses,many=True)
        return Response({'userCourses': course.data}, status=status.HTTP_200_OK)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def updateUserCourse(request):
    user = request.data['userId']
    userCourses = get_object_or_404(UserCourse,userId=user)
    request.data["startDate"] = datetime.now().date()
    courseSerializer = UserCourseSerializer(userCourses, data=request.data)
    if courseSerializer.is_valid(raise_exception=True):
        courseSerializer.save()
        return Response({'message': 'Course Updated Successfully',"userCourses":courseSerializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)