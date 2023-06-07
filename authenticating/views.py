from django.shortcuts import render, redirect
from .emails import *
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
import uuid

def registerAPI(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')            
            email = request.POST.get('email')         
            age = request.POST.get('age')
            qualification = request.POST.get('qualification')
            password = request.POST.get('password')
            print(password + 'Krunal')
            hashed_password = make_password(password)
            print(hashed_password)
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
            user =  User(name=name, email=email, age=age,qualification=qualification, password=hashed_password, is_student=is_student, is_instructor=is_instructor)
        
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
            
            return redirect('/')    
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
            email = request.POST.get('email')
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
# class registerAPI(APIView):
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = UserSerializer(data = data)
#             if serializer.is_valid():                
#                 serializer.save()
#                 OTP_email(serializer.data['email'])
                
#                 return Response({
#                     'status': 200,
#                     'message': 'Successfully registered',
#                     'data': serializer.data,
                    
#                 })
            
#             return Response({
#                     'status': 400,
#                     'message': 'Something is wrong',
#                     'data': serializer.errors,
                    
#                 })  
            
#         except Exception as e:
#             print(e)
              
# class verificationAPI(APIView):
    
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = VerifiedUserSerializer(data = data)
#             if serializer.is_valid():   
#                 email = serializer.data['email']
#                 OTP = serializer.data['OTP']
#                 user = User.objects.filter(email = email)                         
            
#                 try:
#                     if not user.exists():                    
#                         return Response({
#                         'status': 400,
#                         'message': 'Invalid Email',
#                         'data': serializer.data,
#                         })     
#                 except Exception as e:
#                     print(e)     
                              
#                 if user[0].otp != OTP:
#                     return Response({
#                     'status': 400,
#                     'message': 'Wrong OTP',
#                     'data': {},
#                 })
                
#                 user = user.first()
#                 user.is_verified = True
#                 user.save()
                   
#                 return Response({
#                     'status': 200,
#                     'message': 'Successfully registered',
#                     'data': serializer.data,
                    
#                 })
#             return Response({
#                     'status': 400,
#                     'message': 'Something is wrong',
#                     'data': serializer.errors,                    
#                 })  
                
                
#         except Exception as e:
#             print(e)
            
# class LoginAPI(APIView):
    
#     def post(self, request):
#         try:
#             data = request.data
#             serializer = LoginSerializer(data = data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 password = serializer.data['password']
                
#                 try:
#                     user = User.objects.get(email=email)
#                 except User.DoesNotExist:
#                     user = None
                    
#                 if user is None:
#                     return Response({
#                     'status': 400,
#                     'message': 'Invalid Username',
#                     'data': {},                    
#                 })
                
#                 if check_password(password, user.password) is True:
#                     return Response({
#                     'status': 200,
#                     'message': 'Login successful',
#                     'data': serializer.data,                    
#                 })
                
#             return Response({
#                     'status': 400,
#                     'message': 'Something is wrong',
#                     'data': serializer.errors,                    
#                 })  
#         except Exception as e:
#             print(e)

# class forgetpasswordAPI(APIView):
    
#     def post(self,request):
#         try:
#             data = request.data
#             serializer = ForgetPasswordSerializer(data = data)
#             if serializer.is_valid():
#                 email = serializer.data['email']
#                 user = User.objects.filter(email=email).first()
#                 if user:
#                     encoded_pk = urlsafe_b64encode(force_bytes(user.pk))
#                     token = PasswordResetTokenGenerator.make_token(user)
            
#         except Exception as e:
#             print(e)
        