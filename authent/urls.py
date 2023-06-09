from django.urls import path
from authent import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='home2'),
    path('signup/', views.register, name='signup'),
    path('otp/',views.otp, name='otp'),
    path('login/',views.loginAPI, name='login'),
    path('forget-password/',views.forgetpasswordAPI, name='forget-password'),
    path('change_password/<token>/',views.changpasswordAPI, name='change_password'),
    path('accounts/logout/',views.logout_view,name='logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)