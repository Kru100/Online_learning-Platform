from django.urls import path
from conversation import views
from administartion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('students/', views.printUser, name='students'),
    path('instructors/', views.printInstructor, name='instructors'),
    path('courses/', views.printCourse, name='courses'),
    path('payments/<int:course_id>', views.PaymentHandling, name='payment'),
    path('paymentsHandler/', views.PaymentAccept, name='paymentHandler'),
    path('accept_payment/<int:payment_id>', views.accept_payment, name='accept_payment'),
    path('deny_payment/<int:payment_id>', views.deny_payment, name='deny_payment')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)