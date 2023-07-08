from djongo import models

class Anouncement(models.Model):
    sender = models.EmailField()
    anouncement = models.TextField()
    urls = models.URLField(default=None)
    course = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()

class Doubt_ask(models.Model):
    course_id = models.IntegerField()
    sender = models.EmailField()
    doubt = models.TextField(default=None)
    time = models.DateTimeField(auto_now_add=True)
    is_replied = models.BooleanField(default=False)
    reply_id = models.IntegerField(default=None)
    objects = models.DjongoManager()
    
class Doubt_replied(models.Model):
    course_id = models.IntegerField()
    ask_id = models.IntegerField()
    sender = models.EmailField(default=None)
    receiver = models.EmailField()
    reply = models.CharField(max_length=2500)
    time = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()
    
class Help(models.Model):
    email = models.EmailField()
    helpline = models.CharField(max_length=5000)
    is_solve = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()    
    
class Feedback(models.Model):
    course_id = models.IntegerField()
    email = models.EmailField()
    user_name = models.CharField(max_length=100,default=None)
    feedback = models.CharField(max_length=5000)
    star = models.IntegerField(default=None)
    objects = models.DjongoManager()

class Notifications(models.Model):
    course_id = models.IntegerField()
    student = models.IntegerField()
    text = models.TextField()
    is_viewed = models.BooleanField(default=False)
    objects = models.DjongoManager()