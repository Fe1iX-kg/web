from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Основная страница about
    path('about/team/', views.about_team, name='about_team'),  # Подстраница about/team
    path('about/history/', views.about_history, name='about_history'),  # Подстраница about/history
    path('address/', views.address, name='address'),
    path('support/', views.support, name='support'),
    path('contacts/', views.contacts, name='contacts'),
    path('students/<int:student_id>/', views.student_detail, name='students_detail')  # Исправил синтаксис
]