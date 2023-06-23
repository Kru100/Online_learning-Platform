from django.shortcuts import render
from instructor.models import User
from django.contrib.auth.decorators import login_required
from authenticating.views import *


# Create your views here.

@custom_login_required
def indexpage(request):
    email = request.session.get('email')
    user = User.objects.get(email=email)
    return render(request,'home.html',{'user': user})

