from django.core.mail import send_mail
from django.conf import settings
from .models  import *
import random

def OTP_email(email):
    subject = 'Your account Verification'
    OTP = random.randint(1000, 9999)
    message = f'Your OTP is {OTP}'
    send_mail(subject, message, "educator.organiation123@gmail.com", [email],fail_silently=False)
    user_obj = User.objects.get(email=email)
    user_obj.otp = OTP 
    user_obj.save()