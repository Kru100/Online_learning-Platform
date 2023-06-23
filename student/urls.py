from django.urls import path
from . import views

urlpatterns = [
    path('indexpage/',views.indexpage,name='indexpage'),
]
