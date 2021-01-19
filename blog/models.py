from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # Uses default User table of the django and 'on_delete' states the activity to execute when user gets deleted
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
    
