from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Relation(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
