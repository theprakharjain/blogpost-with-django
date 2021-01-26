from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Database Model
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # Uses default User table of the django and 'on_delete' states the activity to execute when user gets deleted
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    # Getting full path of the route
    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk':self.pk})
    
