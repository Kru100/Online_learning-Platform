from django.urls import path
from instructor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add-course/', views.add_course, name='add-course'),
    path('enrolledCourse/',views.enrolledCourse, name='enrollment'),
    path('display/',views.showenrolled, name='display'),
    path('instructor_list/',views.ins_list,name='ins_list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)