from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.task_list, name='task_list')
]