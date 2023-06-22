from django.shortcuts import render, redirect
from .models import *
from instructor.models import *
from django.urls import reverse
from django.contrib import messages

def anounce_home(request, course_id):
    try:
        an = Anouncement.objects.filter(course=course_id).order_by('-time')
        course = Course.objects.get(id=course_id)
        return render(request, 'anouncement_home.html', {'an': an, 'course': course})
    except Exception as e:
        print(e)        

def make_announcement(request, course_id):
    try:
        if request.method == 'POST':
            sender = request.session.get('email')
            anouncement = request.POST.get('anouncement')
            an = Anouncement(sender=sender, anouncement=anouncement, course=course_id)
            an.save()
            messages.add_message(request, messages.INFO, 'Announcement Created successfully!!!')
            return redirect(reverse('annoucement', kwargs={'course_id': course_id}))
        return render(request, 'make-anouncement.html')
    except Exception as e:
        print(e)
