from django.urls import path
from . import views

urlpatterns = [
    path('indexpage/',views.indexpage,name='indexpage'),
    path('search/',views.search_course,name='search'),
    path('course-single/<int:course_id>/',views.course_single,name='course-single'),
    path('enroll/<int:course_id>/',views.enroll_student,name='enrollment'),
]
