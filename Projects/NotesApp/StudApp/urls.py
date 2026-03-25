from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='stud-login'),
    path('signup/', views.signup, name='stud-signup'),
    path('verify-otp/', views.verify_otp, name='verify-otp'),
    path('dashboard/', views.student_dashboard, name='stud-dashboard'),
    path('submit-note/', views.submit_note, name='submit-note'),
    path('logout/', views.logout_view, name='logout'),
]
