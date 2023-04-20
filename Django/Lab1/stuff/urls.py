from django.urls import path

from . import views

app_name = 'stuff'

urlpatterns = [
    path('list', views.list, name='list'),
    path('insert/', views.insert, name='insert'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
