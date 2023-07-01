from django.http import HttpResponse
from django.shortcuts import render
from instructor.models import *
from django.contrib.auth.decorators import login_required
from authent.views import *


# Create your views here.

@custom_login_required
def indexpage(request):
    email = request.session.get('email')

    user = User.objects.get(email=email)
    return render(request,'home.html',{'user': user})

def search_course(request):


    
      query = request.GET['query']
      allcourse = list(Course.objects.filter(name__icontains=query))
      alldescription = list(Course.objects.filter(description__icontains=query))

# Combine the two lists
      result = allcourse + alldescription

# If you want to remove duplicates, you can convert the list to a set and then back to a list
      results = list(set(result))
      context = {
        'results' : results,
     
       }

      return render(request,'search.html',context)

   


    
    