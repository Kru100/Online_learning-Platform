from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def add_course(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            instructor = request.POST.get('instructor')
            user = User.objects.filter(email=instructor).first()
            if user.is_instructor == False:
                msg = "Your have no rights to add course."
                messages.add_message(request, messages.INFO, msg)
                return render(request, 'addcourse.html')
            course = Course(name=name, instructor=instructor)
            course.save()
            msg = "Course added successfully."
            messages.add_message(request, messages.INFO, msg)
            return render(request, 'addcourse.html')
        return render(request, 'addcourse.html')
    except Exception as e:
        print(e)