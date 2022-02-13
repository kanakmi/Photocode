from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime


class blog(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now)
    title = models.CharField(max_length=60)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    topic = models.CharField(max_length=50, null=True, blank=True)


class comments(models.Model):
    blog_page = models.ForeignKey(blog, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_like = models.IntegerField(default=0)
