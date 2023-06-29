from djongo import models

class Anouncement(models.Model):
    sender = models.EmailField()
    anouncement = models.TextField()
    course = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()

class Doubt_ask(models.Model):
    course_id = models.IntegerField()
    sender = models.EmailField()
    doubt = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)
    is_replied = models.BooleanField(default=False)
    objects = models.DjongoManager()
    
class Doubt_replied(models.Model):
    course_id = models.IntegerField()
    ask_id = models.IntegerField()
    receiver = models.EmailField()
    reply = models.CharField(max_length=2500)
    time = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()