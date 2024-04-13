from rest_framework import serializers
from .models import UserCourse

class UserCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourse
        fields = ['userId', 'courseId', 'startDate', 'endDate', 'isCourseStarted']