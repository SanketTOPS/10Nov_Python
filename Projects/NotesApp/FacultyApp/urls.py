from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='fac-login'),
    path('signup/', views.signup, name='fac-signup'),
    path('dashboard/', views.faculty_dashboard, name='fac-dashboard'),
    path('update-status/<int:note_id>/<str:status>/', views.update_note_status, name='update-status'),
]
