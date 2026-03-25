from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('submit-note/', views.submit_note, name='submit_note'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
