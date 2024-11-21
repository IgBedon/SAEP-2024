import os
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 


class Task(models.Model):
    description = models.TextField()
    department_name = models.CharField(max_length=50, blank=True) 
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="A Fazer")
    register_date = models.DateTimeField(default=now) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description
