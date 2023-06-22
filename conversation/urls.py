from django.urls import path
from conversation import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('annoucement/<int:course_id>', views.anounce_home, name='annoucement'),
    path('do-anouncement/<int:course_id>', views.make_announcement, name='do-anouncement')    
]
