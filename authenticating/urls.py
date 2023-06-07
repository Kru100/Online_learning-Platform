from django.urls import path
from authenticating import views

urlpatterns = [
    path('signup/', views.registerAPI, name='signup'),
    path('otp/',views.otp, name='otp'),
    path('login/',views.loginAPI, name='login')
]