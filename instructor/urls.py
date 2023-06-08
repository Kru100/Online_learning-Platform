from django.urls import path
from instructor import views

urlpatterns = [
    path('add-course/', views.add_course, name='add-course')
]