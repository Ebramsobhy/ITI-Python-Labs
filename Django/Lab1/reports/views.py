from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def list_student(request):
    return HttpResponse("This is Student list")

def list_staff(request):
    return HttpResponse("This is Staff list")

def main_report(request):
    student_list_link = reverse('list_student')
    staff_list_link = reverse('list_staff')
    return render(request, 'main_report.html')