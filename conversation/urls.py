from django.urls import path
from conversation import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('annoucement/<int:course_id>/', views.anounce_home, name='annoucement'),
    path('do-anouncement/<int:course_id>/', views.make_announcement, name='do-anouncement'),
    path('ask-doubt/<int:course_id>/', views.ask_doubt, name='ask-doubt'),
    path('reply-doubt/<int:course_id>/<int:ask_id>/', views.reply_doubt, name='reply-doubt'),  
    path('instructor-doubt/<int:course_id>/', views.doubtboard_instructor, name='instructor-doubt'),
    path('student-doubt/<int:course_id>/', views.doubtboard_student, name='student-doubt'),
    path('gethelp', views.getHelp, name='gethelp'),
    path('make-feedback/<int:course_id>', views.make_Feedback, name='make-feedback'),
    path('show-feedback/<int:course_id>', views.show_feedback, name='show-feedback'),
    path('show-help', views.show_help, name='show-help'),
    path('solve-query/<int:id>', views.solve_query, name='solve-query'),
    path('notification-board/<int:course_id>', views.notification_board, name='notification-board'),  
    path('notification', views.notification, name='notification')
]
