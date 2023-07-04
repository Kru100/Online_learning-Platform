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

   


    
    