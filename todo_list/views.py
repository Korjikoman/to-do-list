from http.client import HTTPResponse
from django.shortcuts import render


def task_list(request):
    return render(request, 'todo_list/task_list.html', {})


