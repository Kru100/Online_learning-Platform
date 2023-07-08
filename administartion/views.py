from django.shortcuts import render, redirect
from instructor.models import *

def printUser(request):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()
        if user.is_admin:
            user = User.objects.filter().all()
            return render(request, 'admin-studentlist.html', {'user': user})
        return redirect('/error404')
    except Exception as e:
        print(e)

def printInstructor(request):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()
        if user.is_admin:
            user = User.objects.filter().all()
            return render(request, 'admin-instructorlist.html', {'user': user})
        return redirect('/error404')
    except Exception as e:
        print(e)

def printCourse(request):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()
        if user.is_admin:
            course = Course.objects.filter().all()
            return render(request, 'admin-courselist.html', {'course': course})
        return redirect('/error404')
    except Exception as e:
        print(e)
        
def admin(request):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()
        if user.is_admin:
            return render(request, "home1.html")
        return redirect('/error404')
    except Exception as e:
        print(e)
# Create your views here.
# from django.shortcuts import render, get_object_or404
# from django.http import HttpResponse
# from .models import Course, Enrollment
# import razorpay

# def EnrollmentCreateView(request, course_id):
#     course = get_object_or_404(Course, pk=course_id)
#     client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_SECRET_KEY"))

#     data = {
#         'amount': course.price * 100,  # amount in smallest currency unit
#         'currency': 'INR',
#         'receipt': 'order_rcptid_11',
#         'notes': {
#             'teacher_id': course.teacher.id
#         },
#         'split': [
#             {
#                 'account': course.teacher.razorpay_account_id,
#                 'amount': int(course.price * 0.9 * 100),  # 90% of the course price goes to the teacher
#                 'currency': 'INR',
#                 'description': 'Split for teacher'
#             },
#             {
#                 'account': 'YOUR_RAZORPAY_ACCOUNT_ID',
#                 'amount': int(course.price * 0.1 * 100),  # 10% of the course price goes to the platform
#                 'currency': 'INR',
#                 'description': 'Split for platform'
#             }
#         ]
#     }

#     order = client.order.create(data=data)

#     # If the order was created successfully, create an Enrollment
#     if order:
#         Enrollment.objects.create(student=request.user, course=course)

#     return HttpResponse('Enrollment created')