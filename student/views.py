from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from instructor.models import *
from django.contrib.auth.decorators import login_required
from authent.views import *


# Create your views here.

@custom_login_required
def indexpage(request):
    email = request.session.get('email')

    user = User.objects.get(email=email)
    return render(request, 'home.html', {'user': user})


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
      #  enroll = False

      #  if request.session.get('email'):
      #     enroll = course.enrolled.filter(email=request.session.email).exists()

       context = {
         'course' : course,
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

        # Save the updated course
        course.save()
        
        msg= "You have successfully enrolled. congrats !!"
        messages.add_message(request, messages.INFO, msg)
        # Redirect the user to a success page or course details page

        return redirect(reverse('course-single',kwargs={'course_id': course_id}))
     
     except Exception as e:
        print(e)
          

   


    
    