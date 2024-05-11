from http.client import HTTPResponse
from django.shortcuts import render
from .models import Task
from django.utils import timezone

def task_list(request):
    
    tasks = Task.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'todo_list/task_list.html', {'tasks': tasks})



