from django.db import models

# Create your models here.


class UserCourse(models.Model):
    userId = models.OneToOneField('auth.User', on_delete=models.CASCADE,primary_key=True)
    courseId = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    isCourseStarted = models.BooleanField(default=False)    