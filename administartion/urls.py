from django.urls import path
from conversation import views
from administartion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', views.admin, name='admin'),
    path('students', views.printUser, name='students'),
    path('instructors', views.printInstructor, name='instructors'),
    path('courses', views.printCourse, name='courses'),
]
