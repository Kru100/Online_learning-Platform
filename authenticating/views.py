from django.shortcuts import render, redirect
from .emails import *
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password

is_send = False

def registerAPI(request):
    try:
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
            print(email)
            user1 = User.objects.filter(email=email).first()
            print(user1)
            otp = request.POST.get('otp')
            print(type(otp))
            print(type(user1.otp))
            if user1.otp != int(otp):
                print(1)
                msg = "Invalid OTP"
                messages.add_message(request, messages.INFO, msg)
                return render(request, 'otp.html')
            return redirect('/')
        return render(request, 'otp.html')
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
        