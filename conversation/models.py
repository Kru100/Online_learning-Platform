from djongo import models

class Anouncement(models.Model):
    sender = models.EmailField()
    anouncement = models.TextField()
    course = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()
