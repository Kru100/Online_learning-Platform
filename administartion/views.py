from django.shortcuts import render, redirect
from instructor.models import * 
from conversation.models import * 
from django.http import HttpResponse
from django.contrib import messages
from authent.views import *

@custom_login_required
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

@custom_login_required
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

@custom_login_required
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

@custom_login_required        
def admin(request):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()
        if user.is_admin:
            courses = Course.objects.all()
            total_rev = 0
            for course in courses:
                total_rev += (course.price * course.enrolled.count())
            total_user = User.objects.all().count()
            total_course = Course.objects.all().count()
            context = {
                'total_rev': total_rev,
                'total_user': total_user,
                'total_course': total_course
            }
            return render(request, "home1.html", context)
        return redirect('/error404')
    except Exception as e:
        print(e)

@custom_login_required        
def PaymentHandling(request, course_id):
    try:
        if request.method == 'POST':
            email = request.session.get('email')
            user = User.objects.get(email=email)
            upi = request.POST.get('upi')
            pay = Payment(course_id=course_id, user_id=user.id, payment_id = upi)
            pay.save()
            course = Course.objects.get(id=course_id)    
            return render(request, "payment.html", {'course': course})
        course = Course.objects.get(id=course_id)   
        return render(request, "payment.html", {'course': course})
    except Exception as e:
        print(e)    

@custom_login_required
def PaymentAccept(request):
    try:
        email = request.session.get('email')
        user = User.objects.filter(email=email).first()
        if user.is_admin:
            pay = Payment.objects.all()
            cnt = 0
            data = []
            for p in pay:
                if p.is_done == False:
                    cnt += 1
                    c = Course.objects.get(id=p.course_id)
                    data.append((p, c))               
            return render(request, 'paymentHandle.html', {'cnt': cnt, 'data': data})
        return redirect('/error404')
    except Exception as e:
        print(e) 

@custom_login_required
def accept_payment(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    Notifications.objects.create(course_id=payment.course_id, student=payment.user_id, text="Your Payment is accepted. You can access the course now.")
    payment.is_done = True
    payment.save()
    return redirect('paymentHandler')

@custom_login_required
def deny_payment(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    Notifications.objects.create(course_id=payment.course_id, student=payment.user_id, text="Your Payment is declined. For query contact via Help.")
    payment.delete()
    return redirect('paymentHandler')  
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