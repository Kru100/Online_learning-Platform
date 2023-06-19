from django.urls import path
from instructor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-course/', views.add_course, name='add-course'),
    path('enrolledCourse/',views.enrolledCourse, name='enrollment'),
    path('display/',views.showenrolled, name='display'),
    path('display2/',views.courselist, name='display2'),
    path('course/<int:course_id>/',views.createQuiz, name='course'),
    path('quiz/<int:course_id>/<int:quiz_id>/', views.quizdisplay, name='quiz'),
    path('quizshow/<int:quiz_id>/', views.quiz_show, name='quiz_show'),
    path('video/<int:course_id>/',views.video_upload, name='video_upload')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)