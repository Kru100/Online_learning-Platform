from django.urls import path
from authenticating import views

urlpatterns = [
    path('signup/', views.registerAPI, name='signup'),
    path('otp/',views.otp, name='otp'),
    path('login/',views.loginAPI, name='login'),
    path('forget-password/',views.forgetpasswordAPI, name='forget-password'),
    path('change_password/<token>/',views.changpasswordAPI, name='change_password')
]