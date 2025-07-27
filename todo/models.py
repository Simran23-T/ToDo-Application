# C:\Users\admin\Desktop\BESANT\PYTHON-BASICS\Learning Django\ToDo\todo\models.py

from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
