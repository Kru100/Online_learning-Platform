from django.urls import path
from . import views

urlpatterns = [
    path('indexpage/',views.indexpage,name='indexpage'),
    path('search/',views.search_course,name='search'),
    path('course-single/<int:course_id>/',views.course_single,name='course-single'),
    path('enroll/<int:course_id>/',views.enroll_student,name='enrollment'),
    path('studet-quiz-show/<int:course_id>/<int:quiz_id>',views.student_quiz_show,name='student_quiz_show'),
    path('calculate-marks/<int:quiz_id>/',views.calculate_marks,name='calculate'),
    path('student-videos/<int:course_id>/',views.videos_pagination,name='video-pagination'),
    path('student-profile/',views.student_profile,name='student-profile'),
    path('rating/<int:course_id>/',views.student_feedback,name='student_feedback'),
    path('search/filter/',views.search_filter,name='search_filter'),
]
