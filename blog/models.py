from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)