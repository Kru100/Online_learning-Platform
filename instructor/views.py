from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.urls import reverse
from datetime import date
from django.contrib.auth.decorators import login_required
from authent.views import *

@custom_login_required
def home(request):
    email = request.session.get('email')
    user = User.objects.get(email=email)
    return render(request, 'inst_home.html',{'user': user})

@custom_login_required
def add_course(request):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
            if request.method == 'POST':
                name = request.POST.get('name')
                instructor = request.session.get('email')
                description = request.POST.get('description')
                time_needed = request.POST.get('time_needed')
                created_at = date.today()
                price = request.POST.get('price')
                user = User.objects.filter(email=instructor).first()
                if user.is_instructor == False:
                    msg = "Your have no rights to add course."
                    messages.add_message(request, messages.INFO, msg)
                    return render(request, 'courseadd.html')
                course = Course(name=name, instructor=instructor, description=description, time_needed=time_needed, created_at=created_at, price=price)
                course.save()
                msg = "Course added successfully."
                messages.add_message(request, messages.INFO, msg)
                return render(request, 'courseadd.html')
            return render(request, 'courseadd.html')
        return redirect('error404')
    except Exception as e:
        print(e)
        
def enrolledCourse(request):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
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
        return redirect('error404/')         
    except Exception as e:
        print(e)
        
@custom_login_required
def courselist(request):
    try:
        email = request.session.get('email')
        print(1)
        user = User.objects.get(email=email)
        print(2)
        if user.is_instructor:
            email = request.session.get('email')
            course = Course.objects.filter(instructor=email).all()
            return render(request, 'courselist.html', {'course': course})
        return redirect('error404')
    except Exception as e:
        print(e)
  
@custom_login_required      
def createQuiz(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        if user.is_instructor == True or ta != None:
            if request.method == 'POST':
                quizname = request.POST.get('quizname')
                quiz = Quiz_details.objects.filter(course_id=course_id).all()
                for q in quiz:
                    if q.quiz_name == quizname:
                        messages.add_message(request, messages.INFO, "Quiz already exists.")
                        return redirect(reverse('quizz', kwargs={'course_id': course_id}))
                quiz = Quiz_details(course_id=course_id,quiz_name=quizname)
                quiz.save()
                messages.add_message(request, messages.INFO, "Quiz Added")
                return redirect(reverse('quizz', kwargs={'course_id': course_id}))

            course = Course.objects.get(id=course_id)
            quiz = Quiz_details.objects.filter(course_id=course_id).all()
            context = {
                    'quiz' : quiz,
                    'course' : course,
                    'user':user,
                    'ta' : ta,
                }
            return render(request,'coursehome.html',context)
        return redirect('error404')
    except Exception as e:
        print(e)
        
@custom_login_required
def quizdisplay(request, course_id, quiz_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
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
            context = {
                'id' : course_id,
                'quiz' : quizz,
                'course' : course,
                'quiz1' : quiz1,
            }
            return render(request, 'quizz.html',context)  
        return redirect('error404')  
    except Exception as e:
        print(e)

@custom_login_required
def quiz_show(request,course_id,quiz_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        if user.is_instructor == True or ta != None:
            quizz = Quiz.objects.filter(quiz_id=quiz_id).all()  
            context = {            
                'quiz' : quizz,  
                'user' : user,
                'ta' : ta,         
            }
            return render(request, 'quiz_show.html',context)  
        return redirect('error404')  
    except Exception as e:
        print(e)
       
@custom_login_required       
def video_upload(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email,course_id=course_id).first()
        if user.is_instructor == True or ta != None:
            if request.method == 'POST':
                video_title = request.POST.get('video_title')
                video_description = request.POST.get('video_description')
                file = request.FILES.get('file')
                vid = Video(course_id=course_id, video_title=video_title,video_description=video_description, file=file)
                vid.save()
                messages.add_message(request, messages.INFO, "Video saved successfully.")
                return redirect(reverse('video_upload', kwargs={'course_id': course_id,}))
            vid = Video.objects.filter(course_id=course_id)
            course = Course.objects.get(id=course_id)
            return render(request, 'upload.html', {'vid':vid, 'user':user, 'ta' : ta, 'course':course})
        return redirect('error404')
    except Exception as e:
        print(e)

@custom_login_required
def edit_question(request,course_id,quiz_id,id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        if user.is_instructor == True or ta != None:
            quizz = Quiz.objects.get(id=id)
            context = {
                 'quizz' : quizz,
                 'user' : user,
                 'ta' : ta,
            }
            return render(request,'update.html',context)
        return redirect('error404')
    except Exception as e:
        print(e)

@custom_login_required
def update_question(request,course_id,quiz_id,id):    
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        if user.is_instructor == True or ta != None:
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
            return render(request,'update.html', {'user': user, 'ta' : ta})
        return redirect('error404')
    except Exception as e:
        print(e)

@custom_login_required
def delete_question(request,course_id,quiz_id,id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
            quizz = Quiz.objects.get(id=id)
            quizz.delete()     
            messages.add_message(request, messages.INFO, "Question deleted successfully !!")
            return redirect(reverse('quiz_show',kwargs={'quiz_id': quiz_id}))
        return redirect('error404')
    except Exception as e:
        print(e)

@custom_login_required
def courseHome(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        ta = TA.objects.filter(email=email, course_id=course_id).first()
        if user.is_instructor == True or ta != None:
            course = Course.objects.get(id=course_id)
            enrolled_users = course.enrolled.all()
            context = {
                'course': course,
                'enrolled_users': enrolled_users,
            }
            if ta != None:
                if ta.is_TA == True:
                    context['ta'] = ta
                    return render(request, 'course.html', context)
            else:
                context['user'] = user
            return render(request, 'course.html', context)
        return redirect('/error404/')
    except Exception as e:
        print(e)

@custom_login_required            
def delete_course(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
            course = Course.objects.get(id=course_id)
            course.delete()
            messages.add_message(request, messages.INFO, "Course deleted successfully !!")
            return redirect('/display2/')
        return redirect('error404')
    except Exception as e:
        print(e)            

@custom_login_required
def edit_course(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
            if request.method == 'POST':
                name = request.POST.get('name')
                instructor = request.session.get('email')
                description = request.POST.get('description')
                time_needed = request.POST.get('time_needed')
                price = request.POST.get('price')
                created_at = date.today()
                course = Course(name=name, instructor=instructor, description=description, time_needed=time_needed, created_at=created_at, price=price)
                course.save()
                msg = "Course added successfully."
                messages.add_message(request, messages.INFO, msg)
                return redirect(reverse('course',kwargs={'course_id': course_id}))
                #return redirect(reverse('quiz_show',kwargs={'quiz_id': quiz_id}))
            return render(request, 'edit_course.html')
        return redirect('error404')
    except Exception as e:
        print(e)
        
def error404(request):
    return render(request, 'error404.html')

@custom_login_required
def TA_add(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor:
            if request.method == 'POST':
                email = request.POST.get('email')
                user = User.objects.get(email=email)
                if user.is_verified != True:
                    messages.add_message(request, messages.INFO, "TA must be registered!!!")
                    return render(request, 'add-TA.html')
                user = TA(email=email, course_id=course_id, is_TA=True)
                user.save()
                return redirect(reverse('TA-list', kwargs={'course_id': course_id}))
            return render(request, 'add-TA.html')
        return redirect('error404')
    except Exception as e:
        print(e)    
        
@custom_login_required
def TA_list(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor:
            ta = TA.objects.filter(course_id=course_id).all()
            course = Course.objects.get(id=course_id)
            return render(request, 'TA-list.html', {'ta': ta, 'course': course})
        return redirect('error404')
    except Exception as e:
        print(e)     
   
@custom_login_required            
def delete_TA(request, course_id, id):
    try:
        email = request.session.get('email')
        user = User.objects.get(email=email)
        if user.is_instructor == True:
            ta = TA.objects.get(id=id)
            ta.delete()
            messages.add_message(request, messages.INFO, "TA deleted successfully !!")
            return redirect(reverse('TA-list', kwargs={'course_id': course_id}))
        return redirect('error404')
    except Exception as e:
        print(e)   
        
@custom_login_required
def course_list_TA(request):
    try:
        email = request.session.get('email')
        ta = TA.objects.get(email=email)
        if ta.is_TA == True:
            ta = TA.objects.filter(email=email).all()
            course=[]
            for t in ta:
                c = Course.objects.get(id=t.course_id)
                course.append(c)
            return render(request, 'courselistTA.html', {'course': course})
        return redirect('error404')
    except Exception as e:
        print(e)   

@custom_login_required
def Revenue(request):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()
        if user.is_instructor:
            courses = Course.objects.filter(instructor=email).all()
            data = [(course.name, (course.price * course.enrolled.count()))for course in courses]
            return render(request, "revenue.html", {'data': data})
        return redirect('/error404')
    except Exception as e:
        print(e)
        
@custom_login_required
def addPayment(request, course_id):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()        
        if user.is_instructor:
            if request.method == 'POST':
                course = Course.objects.get(id=course_id)
                course.file = request.FILES.get('qr')
                course.save()
                messages.add_message(request, messages.INFO, 'Your Payment is now available.')
                return render(request, 'addPayment.html', {'course': course})
                #return redirect(reverse('course', kwargs={'course_id': course_id}))
            return render(request, 'addPayment.html')
        return redirect('/error404')
    except Exception as e:
        print(e)