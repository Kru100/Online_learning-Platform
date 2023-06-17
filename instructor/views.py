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
        
def enrolledCourse(request):
    try:
        if request.method == 'POST':
            coursename = request.POST.get('coursename')
            enrolled = request.POST.get('enrolled')
            course = Course.objects.filter(name=coursename).first()
            user = User.objects.filter(email=enrolled).first()
            print(course)
            print(user)
            course.enrolled.add(user)
            course.save()
            print(course.enrolled)
            msg = "Enrolled successfully."
            messages.add_message(request, messages.INFO, msg)
            return render(request, 'enrolled.html')
        return render(request, 'enrolled.html')            
        
    except Exception as e:
        print(e)
        
def showenrolled(request):
    course = Course.objects.get(name='Krunal')
    enrolled_users = course.enrolled.all()
    context = {
        'course': course,
        'enrolled_users': enrolled_users
    }
    return render(request, 'enrolled_users.html', context)
        
def courselist(request):
    try:
        email = request.session.get('email')
        course = Course.objects.filter(instructor=email).all()
        print(course)
        return render(request, 'courselist.html', {'course': course})
    except Exception as e:
        print(e)