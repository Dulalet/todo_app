from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    deadline = models.DateTimeField(blank=True, null=True)
    executed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

