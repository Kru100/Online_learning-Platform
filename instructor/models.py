from djongo import models
        
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
    enrolled = models.ArrayReferenceField(
        to=User,
        on_delete=models.CASCADE,
        default=None,
    )
    objects = models.DjongoManager()
