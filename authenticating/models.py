from djongo import models

# class subject(models.Model):
#     name = models.CharField(max_length=50)
#     instructor_username = models.CharField(max_length=50)
#     is_allowed = models.BooleanField(default=False)
#     link = models.URLField(blank=True, null=True)
#     duration = models.IntegerField()
#     description = models.TextField()
#     is_active = models.BooleanField(default=False)
    
#     class Meta:
#         abstract = True
        
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    qualification = models.TextField()
    is_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    password = models.CharField(max_length=64)
    otp = models.IntegerField(default = 0)
    token = models.CharField(max_length=100, default=None)
    objects = models.DjongoManager()