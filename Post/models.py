from django.db import models
from User.models import UserProfile

# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:10]

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(UserProfile, related_name='likes', blank=True)
    comments = models.ManyToManyField(Comment, related_name='comments', blank=True)

    def __str__(self):
        return self.text[:10]
