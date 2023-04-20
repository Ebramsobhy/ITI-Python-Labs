from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def list(request):
    return HttpResponse("Stuff List")

def insert(request): 
        return JsonResponse({'id': 1, 'name': 'Ebram', 'age': '24', 'message': 'This is Insert'})

def update(request):
        return JsonResponse({'id': 1, 'name': 'Ebram', 'age': '24', 'message': 'This is Update'})

def delete(request):
     return redirect('stuff:list')
