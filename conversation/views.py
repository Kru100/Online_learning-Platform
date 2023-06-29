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

def ask_doubt(request, course_id):
    try:
        if request.method == 'POST':
            sender = request.session.get('email')
            doubt = request.POST.get('doubt')
            # if len(doubt)>1000:
            #     messages.add_message(request, messages.INFO, 'Only 1000 words allowed!!!')
            #     return render(request, 'ask-doubt.html')
            d = Doubt(sender=sender, doubt=doubt, course=course_id)
            d.save()
            user = User.objects.get(email=sender)
            print(user)
            print(user.is_student)
            if user.is_student == True:
                return redirect(reverse('doubt-index-student', kwargs={'course_id': course_id})) 
            else:
                return redirect(reverse('doubt-index-instructor', kwargs={'course_id': course_id})) 
        return render(request, 'ask-doubt.html')       
    except Exception as e:
        print(e)
        
def reply_doubt(request, course_id, doubt_id):
    try:
        if request.method == 'POST':
            rcv = request.session.get('email')
            reply = request.POST.get('reply')
            d = Doubt.objects.get(id=doubt_id)
            d.rcv = rcv
            d.reply = reply
            d.is_replied = True
            d.save()
            print(d.is_replied)
            user = User.objects.get(email=rcv)
            
            if user.is_student == True:
                return redirect(reverse('doubt-index-student', kwargs={'course_id': course_id})) 
            else:
                return redirect(reverse('doubt-index-instructor', kwargs={'course_id': course_id})) 
        return render(request, 'reply.html')
    except Exception as e:
        print(e)
        
def doubtboard_for_instructor(request, course_id):
    try:
        print(1)
        d = Doubt.objects.filter(course=course_id, is_replied = False).order_by('time')
        #d = d.filter(is_replied=False)
        course = Course.objects.get(id=course_id)
        print(3)
        return render(request, 'doubtboard_instructor.html', {'doubts': d, 'course': course})
    except Exception as e:
        print(e)
        
def doubtboard_for_student(request, course_id):
    try:
        print(1)
        email = request.session.get('email')
        print(2)
        d = Doubt.objects.filter(course=course_id, sender=email).order_by('time')
        print(3)
        course = Course.objects.get(id=course_id)
        print(4)
        return render(request, 'doubtboard_student.html', {'doubts': d, 'course': course})
    except Exception as e:
        print(e)