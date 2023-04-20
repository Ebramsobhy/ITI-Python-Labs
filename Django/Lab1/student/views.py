from django.shortcuts import render, redirect
from django.http import HttpResponse


def list(request):
        return HttpResponse("Student list")

def insert(request):
        return render(request, 'insert.html')

def update(request):
        return render(request, 'update.html')

def delete(request):
        return redirect('student:list')
