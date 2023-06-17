from django.urls import path
from instructor import views

urlpatterns = [
    path('add-course/', views.add_course, name='add-course'),
    path('enrolledCourse/',views.enrolledCourse, name='enrollment'),
    path('display/',views.showenrolled, name='display'),
    path('display2/',views.courselist, name='display2'),
    path('course/<int:course_id>/',views.createQuiz, name='course'),
    path('quiz/<int:course_id>/<int:quiz_id>/', views.quizdisplay, name='quiz')
]