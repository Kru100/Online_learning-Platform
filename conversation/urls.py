from django.urls import path
from conversation import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('annoucement/<int:course_id>/', views.anounce_home, name='annoucement'),
    path('do-anouncement/<int:course_id>/', views.make_announcement, name='do-anouncement'),
    path('ask-doubt/<int:course_id>/', views.ask_doubt, name='ask-doubt'),
    path('reply-doubt/<int:course_id>/<int:doubt_id>/', views.reply_doubt, name='reply-doubt'),  
    path('doubt-index-student/<int:course_id>/', views.doubtboard_for_student, name='doubt-index-student'),
    path('doubt-index-instructor/<int:course_id>/', views.doubtboard_for_instructor, name='doubt-index-instructor')    
]
