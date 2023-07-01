from djongo import models
#from authent.models import *

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    qualification = models.TextField()
    is_registered = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    password = models.CharField(max_length=64)
    otp = models.IntegerField(default = 0)
    token = models.CharField(max_length=100, default=None)
    objects = models.DjongoManager()

class Course(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.EmailField()
    description = models.CharField(max_length=250, default = None)
    time_needed = models.CharField(max_length=100, default=None)
    created_at = models.DateTimeField(default=None)
    price = models.IntegerField(default=0)
    enrolled = models.ArrayReferenceField(
        to=User,
        on_delete=models.CASCADE,
        default = None
    )
    objects = models.DjongoManager()
    
class Quiz_details(models.Model):
    course_id = models.IntegerField()
    quiz_name = models.CharField(max_length=100)
    marks = models.JSONField(default=None)
    time = models.CharField(max_length=100)
    objects = models.DjongoManager()
    
class Quiz(models.Model):
    course_id = models.IntegerField()
    quiz_id = models.IntegerField(default=0)
    question = models.CharField(max_length=500)
    opt1 = models.CharField(max_length=250)
    opt2 = models.CharField(max_length=250)
    opt3 = models.CharField(max_length=250)
    opt4 = models.CharField(max_length=250)
    answer = models.IntegerField()
    objects = models.DjongoManager()

class Video(models.Model):
    course_id = models.IntegerField()
    video_title = models.CharField(max_length=100)
    video_description = models.CharField(max_length=500)
    file = models.FileField(upload_to='videos/%y')  
    objects = models.DjongoManager()      

    