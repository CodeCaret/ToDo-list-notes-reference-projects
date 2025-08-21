from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Task(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    about = models.TextField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # ForeignKey field to associate tasks with a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

