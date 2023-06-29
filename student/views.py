from django.shortcuts import render
from instructor.models import *
from django.contrib.auth.decorators import login_required
from authent.views import *


# Create your views here.

@custom_login_required
def indexpage(request):
    email = request.session.get('email')
    user = User.objects.get(email=email)
    return render(request,'home.html',{'user': user})

