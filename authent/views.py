from django.shortcuts import render, redirect
from instructor.models import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
import uuid
from .emails import *
from datetime import datetime


def index(request):
    return render(request,'homepage.html')

def register(request):
    try:
        user = User.objects.filter().all()
        for u in user:
            if u.is_verified == False:
                u.delete()
        if request.method == 'POST':
            name = request.POST.get('name')          
            email = request.POST.get('email')         
            age = request.POST.get('age')
            qualification = request.POST.get('qualification')
            password = request.POST.get('password')
            hashed_password = make_password(password)
            role = request.POST.get('role')
            if role == 'student':
                is_student = True
                is_instructor = False
            if role == 'instructor':
                is_instructor = True
                is_student = False   
            user1 = User.objects.filter(email=email).first()
            if user1 is not None:
                message = "Email already in used."
                messages.add_message(request, messages.INFO, message)
                return render(request, 'signup.html') 
            user = User.objects.create(name=name, email=email, age=age,qualification=qualification, password=hashed_password, is_student=is_student, is_instructor=is_instructor)
            user.save()
            request.session['email'] = email
            OTP_email(email)
            
            return redirect('otp')
        
        return render(request, 'signup.html')
            
    except Exception as e:
        print(e)

     
def otp(request):
    try:
        if request.method == 'POST':
            email = request.session.get('email')
            user1 = User.objects.filter(email=email).first()
            otp = request.POST.get('otp')
            if user1.otp != int(otp):
                msg = "Invalid OTP"
                messages.add_message(request, messages.INFO, msg)
                return render(request, 'otp.html')
            user1.is_verified = True
            user1.save()
            return redirect('login')
        return render(request, 'otp.html')
    except Exception as e:
        print(e)

     
def loginAPI(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.filter(email=email).first()
            if user is None:
                msg = 'Invalid Email or Password'
                messages.add_message(request, messages.INFO, msg)                
                return render(request, 'login.html')
            if user.is_verified is False:
                msg = 'Verify Your Account'
                messages.add_message(request, messages.INFO, msg)                
                return render(request, 'login.html')
            if user.email != email or check_password(password,user.password) is False:
                msg = 'Invalid Email or Password'
                messages.add_message(request, messages.INFO, msg)
                return render(request, 'login.html')
            
            request.session['email'] = email
            if user.is_student is True:
                return redirect('/indexpage/')
            elif user.is_instructor is True:
                return redirect('/home/')
            else:
                return redirect('/admin/')    
        return render(request, 'login.html')
    except Exception as e:
        print(e)


def changpasswordAPI(request,token):
    context = {}
    try:
        if request.method == 'POST':
            print(1)
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            user = User.objects.filter(token=token).first()
            print(user)
                
            if password != confirm_password:
                msg = 'Both Passwords must be matched.'
                messages.add_message(request, messages.INFO, msg)
                return redirect(f'confirm_password/{token}')
            
            user.password = make_password(password)
            user.save()     
            return redirect('login')  
        context = {'user_id': user.email}        
        return redirect(f'confirm_password/{token}',context)               
        
    except Exception as e:
        print(e)
    return render(request, 'confirmpassword.html') 


def forgetpasswordAPI(request):
    try: 
        if request.method == 'POST':
            email = request.POST.get('email')
            user = User.objects.filter(email=email).first()
            if user is None:
                msg = 'Invalid Email or Password'
                messages.add_message(request, messages.INFO, msg)                
                return render(request, 'forgetpassword.html')
            token = str(uuid.uuid4())
            user.token = token
            user.save()
            Forget_password(email,token)
            msg = f'Email is sent successfully to {email}'
            messages.add_message(request, messages.INFO, msg)
            return render(request, 'forgetpassword.html')
        return render(request, 'forgetpassword.html')              
    except Exception as e:
        print(e)       

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    del request.session['email']  
    logout(request)
    return redirect('login')

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        email = request.session.get('email')
        if email:
            # User is authenticated based on the email session value
            return view_func(request, *args, **kwargs)
        else:
            # User is not authenticated, redirect to the login page
            return redirect('login')
    
    return wrapper