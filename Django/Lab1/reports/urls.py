from django.urls import path
from . import views

urlpatterns = [
    path('liststudent/', views.list_student, name='list_student'),
    path('liststaff/', views.list_staff, name='list_staff'),
    path('mainreport/', views.main_report, name='main_report'),
]
