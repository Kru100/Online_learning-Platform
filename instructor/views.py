from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from datetime import date
def add_course(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            instructor = request.session.get('email')
            description = request.POST.get('description')
            time_needed = request.POST.get('time_needed')
            created_at = date.today()
            user = User.objects.filter(email=instructor).first()
            if user.is_instructor == False:
                msg = "Your have no rights to add course."
                messages.add_message(request, messages.INFO, msg)
                return render(request, 'courseadd.html')
            course = Course(name=name, instructor=instructor, description=description, time_needed=time_needed, created_at=created_at)
            course.save()
            msg = "Course added successfully."
            messages.add_message(request, messages.INFO, msg)
            return render(request, 'courseadd.html')
        return render(request, 'courseadd.html')
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
        return render(request, 'courselist.html', {'course': course})
    except Exception as e:
        print(e)
      
def createQuiz(request, course_id):
    try:
        if request.method == 'POST':
            quizname = request.POST.get('quizname')
            total_marks = request.POST.get('total_marks')
            time = request.POST.get('time')
            quiz = Quiz_details.objects.filter(course_id=course_id).all()
            print(1)
            for q in quiz:
                print(2)
                if q.quiz_name == quizname:
                    print(3)
                    messages.add_message(request, messages.INFO, "Quiz already exists.")
                    return redirect(reverse('course', kwargs={'course_id': course_id}))
            print(4)
            quiz = Quiz_details(course_id=course_id,quiz_name=quizname,total_marks=total_marks,time=time)
            print(5)
            quiz.save()
            messages.add_message(request, messages.INFO, "Quiz Added")
            return redirect(reverse('course', kwargs={'course_id': course_id}))
        
        course = Course.objects.get(id=course_id)
        quiz = Quiz_details.objects.filter(course_id=course_id).all()
        context = {
                'quiz' : quiz,
                'course' : course,
            }
        return render(request,'coursehome.html',context)
    except Exception as e:
        print(e)
        
def quizdisplay(request, course_id, quiz_id):
    try:
        if request.method == 'POST':       
            question = request.POST.get('question')
            opt1 = request.POST.get('opt1')
            opt2 = request.POST.get('opt2')
            opt3 = request.POST.get('opt3')
            opt4 = request.POST.get('opt4')
            answer = request.POST.get('answer')
            
            quiz = Quiz(course_id = course_id,quiz_id = quiz_id,question=question, opt1=opt1, opt2=opt2, opt3=opt3, opt4=opt4, answer=answer)
            quiz.save()
            return redirect(reverse('quiz', kwargs={'course_id': course_id, 'quiz_id': quiz_id}))
            #redirect(reverse('course', kwargs={'course_id': course_id}))
        course = Course.objects.get(id=course_id)
        quiz1 = Quiz_details.objects.get(id=quiz_id)
        quizz = Quiz.objects.filter(quiz_id=quiz_id).all()
        print(quizz)
        context = {
            'id' : course_id,
            'quiz' : quizz,
            'course' : course,
            'quiz1' : quiz1,
        }
        return render(request, 'quizz.html',context)    
    except Exception as e:
        print(e)

def quiz_show(request,quiz_id):
      
        quizz = Quiz.objects.filter(quiz_id=quiz_id).all()
  
        context = {
            
            'quiz' : quizz,
           
        }
        return render(request, 'quiz_show.html',context)    
       
def video_upload(request, course_id):
    if request.method == 'POST':
        video_title = request.POST.get('video_title')
        video_description = request.POST.get('video_description')
        file = request.FILES.get('file')
        vid = Video(course_id=course_id, video_title=video_title,video_description=video_description, file=file)
        vid.save()
        messages.add_message(request, messages.INFO, "Video saved successfully.")
        return redirect(reverse('video_upload', kwargs={'course_id': course_id,}))
    vid = Video.objects.filter(course_id=course_id)
    return render(request, 'upload.html', {'vid':vid,})