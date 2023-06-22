from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from datetime import date

def home(request):
    email = request.session.get('email')
    user = User.objects.get(email=email)
    return render(request, 'inst_home.html',{'user': user})

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
            course = Course.objects.get(name=coursename)
            user = User.objects.get(email=enrolled)
            print(course)
            print(user)
            print(1)
            course.enrolled.add(user)
            print(2)
            msg = "Enrolled successfully."
            messages.add_message(request, messages.INFO, msg)
            return render(request, 'enrolled.html')
        return render(request, 'enrolled.html')            
        
    except Exception as e:
        print(e)
        
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
            for q in quiz:
                if q.quiz_name == quizname:
                    messages.add_message(request, messages.INFO, "Quiz already exists.")
                    return redirect(reverse('quizz', kwargs={'course_id': course_id}))
            quiz = Quiz_details(course_id=course_id,quiz_name=quizname,total_marks=total_marks,time=time)
            quiz.save()
            messages.add_message(request, messages.INFO, "Quiz Added")
            return redirect(reverse('quizz', kwargs={'course_id': course_id}))
        
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
    try:
        quizz = Quiz.objects.filter(quiz_id=quiz_id).all()  
        context = {            
            'quiz' : quizz,           
        }
        return render(request, 'quiz_show.html',context)    
    except Exception as e:
        print(e)
       
def video_upload(request, course_id):
    try:
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
    except Exception as e:
        print(e)


def edit_question(request,course_id,quiz_id,id):
    try:
        quizz = Quiz.objects.get(id=id)
        context = {
             'quizz' : quizz
        }
        return render(request,'update.html',context)
    except Exception as e:
        print(e)

def update_question(request,course_id,quiz_id,id):    
    try:
        if request.method == 'POST' :
            questions = request.POST.get('question')
            opt1s = request.POST.get('opt1')
            opt2s = request.POST.get('opt2')
            opt3s = request.POST.get('opt3')
            opt4s = request.POST.get('opt4')
            answer = request.POST.get('answer')

            quizz = Quiz.objects.get(id=id)

            quizz.question = questions
            quizz.opt1 = opt1s
            quizz.opt2 = opt2s
            quizz.opt3 = opt3s
            quizz.opt4 = opt4s
            quizz.answer = answer

            quizz.save()
            messages.add_message(request, messages.INFO, "Question updated successfully !!")
            return redirect(reverse('quiz_show',kwargs={'quiz_id': quiz_id}))
        return render(request,'update.html')
    except Exception as e:
        print(e)

def delete_question(request,course_id,quiz_id,id):
    try:
        quizz = Quiz.objects.get(id=id)
        quizz.delete()     
        messages.add_message(request, messages.INFO, "Question deleted successfully !!")
        return redirect(reverse('quiz_show',kwargs={'quiz_id': quiz_id}))
    except Exception as e:
        print(e)

def courseHome(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        enrolled_users = course.enrolled.all()
        #print(len(course.enrolled))
        context = {
            'course': course,
            'enrolled_users': enrolled_users
        }
        return render(request, 'course.html', context)
    except Exception as e:
        print(e)
            
def delete_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
        course.delete()
        messages.add_message(request, messages.INFO, "Course deleted successfully !!")
        return redirect('/display2/')
    except Exception as e:
        print(e)            
            

            
   

