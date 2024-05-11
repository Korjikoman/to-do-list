from django.db import models
from django.conf import settings
from django.utils import timezone

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    created_date = models.DateField(default=timezone.now)
    task_done = models.BooleanField(default=False)
    
    
    def done(self):
        self.task_done = True
        self.save()
    
    def __str__(self) -> str:
        return self.text
