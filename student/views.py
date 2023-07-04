from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from instructor.models import *
from django.contrib.auth.decorators import login_required
from authent.views import *
from django.core.paginator import Paginator


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
      
# If you want to remove duplicates, you can convert the list to a set and then back to a list 
      context = {
        'results' : results,
     
       }

      return render(request,'search.html',context)


def course_single(request,course_id):
    
   try: 
       course = Course.objects.get(id=course_id)
       quiz = Quiz_details.objects.filter(course_id=course_id).all()
       videos = Video.objects.filter(course_id=course_id).all()
       enrolled_length = len(course.enrolled.all())
      #  enroll = False

      #  if request.session.get('email'):
      #     enroll = course.enrolled.filter(email=request.session.email).exists()

       context = {
         'course' : course,
          'quizs' : quiz,
         'videos' : videos,
         'length' : enrolled_length,
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
       
      
        quizz = Quiz.objects.filter(quiz_id=quiz_id)

        context ={
        'quizs' : quizz,
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
    
def videos_pagination(request,course_id):
    
     videos = Video.objects.filter(course_id=course_id)
     paginator = Paginator(videos, 1)  # 1 video per page

     page_number = request.GET.get('page')  # Get the page number from the request's GET parameters
     page_obj = paginator.get_page(page_number)  # Get the corresponding page object

     context = {
        'videos': page_obj,
        'course_id' : course_id,
     }

     return render(request, 'videos.html', context)
    

        


    
    