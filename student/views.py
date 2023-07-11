from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from instructor.models import *
from django.contrib.auth.decorators import login_required
from authent.views import *
from django.core.paginator import Paginator
from conversation.models import *
import json
from datetime import datetime

# Create your views here.

@custom_login_required
def indexpage(request):
    email = request.session.get('email')

    user = User.objects.get(email=email)

    courses = user.enrolled_courses.all()

    return render(request, 'home.html', {'user': user , 'courses' : courses})


def search_course(request):


      query = request.GET['query']
      allcourse = list(Course.objects.filter(name__icontains=query))
      alldescription = list(Course.objects.filter(description__icontains=query))
      allinstructor = User.objects.filter(name__icontains=query)

      instructors_courses_list = []

      for instructor in allinstructor:
       instructor_courses = list(Course.objects.filter(instructor=instructor.email))
       for course in instructor_courses: 
         instructors_courses_list += instructor_courses

# Combine the two lists
      results = instructors_courses_list + allcourse + alldescription
      results = set(results)

      results_list = [
     {
        'id' : res.id,
        'name': res.name,
        'instructor_name': res.instructor_name,
        'description': res.description,
        'rating': res.rating,
        'price': res.price,
        'rated' : res.rated,
        'created_at': res.created_at.strftime('%d %B, %Y').lstrip('0'),
        'time_needed' : res.time_needed,
        # Add other relevant fields
     }
     for res in results
     ]
      request.session['search_results'] = results_list
      sort_by = ""
      
# If you want to remove duplicates, you can convert the list to a set and then back to a list 
      context = {
        'results' : results,
        'sort_by' : sort_by,
       }

      return render(request,'search.html',context)

def search_filter(request):
    
    results = request.session.get('search_results')
    sort_by = request.GET['sort']
    print(sort_by)

    if sort_by == 'reviewed':
       results.sort(key=lambda x: x['rated'], reverse=True)
    elif sort_by == 'rated':
       results.sort(key=lambda x: x['rating'], reverse=True)
    elif sort_by == 'price':
       results.sort(key=lambda x: x['price'], reverse=True)
    elif sort_by == 'newest':
       results.sort(key=lambda x: datetime.strptime(x['created_at'], '%d %B, %Y'), reverse=True)

      

    context = {
         'results' : results,
         'sort_by' : sort_by,
    }

    return render(request,'search.html',context)



def course_single(request,course_id):
    
   try: 
       course = Course.objects.get(id=course_id)
       quiz = Quiz_details.objects.filter(course_id=course_id).all()
       videos = Video.objects.filter(course_id=course_id).all()
       enrolled_length = len(course.enrolled.all())
       feedback = Feedback.objects.filter(course_id=course_id)

      #  enroll = False

      #  if request.session.get('email'):
      #     enroll = course.enrolled.filter(email=request.session.email).exists()

       context = {
         'course' : course,
          'quizs' : quiz,
         'videos' : videos,
         'length' : enrolled_length,
         'feedback' : feedback,
      #    'enrolled' : enroll,
        }

       return render(request,'course-single.html',context)
    
   except Exception as e:
        print(e)
        


def enroll_student(request, course_id):
  

     try:
        # Retrieve the current user
        email = request.session.get('email')

        user = User.objects.get(email=email)

        # Retrieve the course to enroll in
        course = Course.objects.get(id=course_id)

        # Add the user to the enrolled array of the course
        course.enrolled.add(user)

        user.enrolled_courses.add(course)

        # Save the updated course
        course.save()
        
        msg= "You have successfully enrolled. congrats !!"
        messages.add_message(request, messages.INFO, msg)
        # Redirect the user to a success page or course details page

        return redirect(reverse('course-single',kwargs={'course_id': course_id}))
     
     except Exception as e:
        print(e)

def student_quiz_show(request,course_id,quiz_id):
    
   try:
       
      
        quizz = list(Quiz.objects.filter(quiz_id=quiz_id))
        q = Quiz_details.objects.get(id=quiz_id)
        random.shuffle(quizz)

        context ={
        'quizs' : quizz,
        'q' : q,
       }

        return render(request,'stu_quiz_show.html',context)
          
   except Exception as e:
        print(e)

def calculate_marks(request,quiz_id):
    
    if request.method == 'POST':
        
        total_marks = 0
        paper_marks = 0
        answers = []

        for key, value in request.POST.items():
          if key.startswith('quiz') and key != 'csrfmiddlewaretoken':

            question_id = key[4:]
            answer = int(value) 
            
            question = Quiz.objects.get(id=question_id)

            if answer == question.answer:
                total_marks += question.marks
                paper_marks += question.marks
                
            else:
                    paper_marks += question.marks

            answers.append((question.question, answer, question.answer, 
                            question.opt1,question.opt2,
                            question.opt3,question.opt4))  

        context = {
          'marks' : total_marks,
          'paper_marks' : paper_marks,
          'answers': answers
        }
                   
        return render(request,'correct_answer.html',context)
    paper_marks = 0
    answers = Quiz.objects.filter(quiz_id=quiz_id).all()
    context = {
          'paper_marks' : paper_marks,
          'answers': answers
        }
    return render(request,'correct_answer.html',context)

def videos_pagination(request,course_id):
    
     videos = Video.objects.filter(course_id=course_id)
     paginator = Paginator(videos, 1)  # 1 video per page

     page_number = request.GET.get('page')  # Get the page number from the request's GET parameters
     page_obj = paginator.get_page(page_number)  # Get the corresponding page object

     context = {
        'videos': page_obj,
        'course_id' : course_id,
        'videos2' : videos,
     }

     return render(request, 'videos.html', context)

def student_profile(request):
  try:
    email = request.session.get('email')
    user = User.objects.get(email=email)
    notify = Notifications.objects.filter(student=user.id).all()
    new_notifications = False
    for n in notify:
      if n.is_viewed == False:
        new_notifications = True
        break;
    context = {
        'user' : user,
        'new_notifications' : new_notifications,
    }
    return render(request,'student_profile.html',context)
  except Exception as e:
    print(e)



def student_feedback(request,course_id):
     
     if request.method == 'POST':
       user_email =  request.session.get('email')
       rating = request.POST.get('rate')
       feed = request.POST.get('feedback')
       user = User.objects.get(email=user_email)
       course = Course.objects.get(id=course_id)

       feedback_user = Feedback(course_id=course_id,email=user_email,user_name=user.name,feedback=feed,star=rating)
       feedback_user.save()

       all_feedback = Feedback.objects.filter(course_id=course_id).values('star')
       total_star = sum(feedback['star'] for feedback in all_feedback)
      
       feedback_count = all_feedback.count()
      
       avg = total_star/feedback_count
     
       rounded_avg = round(avg, 1)

       course.rating = rounded_avg
       course.rated = feedback_count
       course.save()
           
     return redirect(reverse('course-single',kwargs={'course_id': course_id}))
     
def cheated(request):
   return render(request, 'cheated.html')
 


   


    
    