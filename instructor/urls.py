from django.urls import path
from instructor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home, name='home'),
    path('add-course/', views.add_course, name='add-course'),
    path('enrolledCourse/',views.enrolledCourse, name='enrollment'),
    path('display2/',views.courselist, name='display2'),
    path('quiz/<int:course_id>/',views.createQuiz, name='quizz'),
    path('quiz/<int:course_id>/<int:quiz_id>/', views.quizdisplay, name='quiz'),
    path('quizshow/<int:quiz_id>/', views.quiz_show, name='quiz_show'),
    path('video/<int:course_id>/',views.video_upload, name='video_upload'),
    path('quiz/update1/<int:course_id>/<int:quiz_id>/<int:id>/',views.edit_question,name='edit_question'),
    path('quiz/update2/<int:course_id>/<int:quiz_id>/<int:id>/',views.update_question,name='update_question'),
    path('quiz/delete/<int:course_id>/<int:quiz_id>/<int:id>/',views.delete_question,name='delete_question'),
    path('course/<int:course_id>/',views.courseHome, name='course'),
    path('course/delete/<int:course_id>', views.delete_course, name='delete_course'),
    path('edit-course/<int:course_id>', views.edit_course, name='edit_course'),
    path('error404', views.error404, name='error404'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)