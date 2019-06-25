from  __future__  import unicode_literals
from django.db import models


class Post(models.Model):
    title= models.CharField(max_length=200)
    text=models.TextField()

class Comment(models.Model):
    name=models.CharField(max_length=100)
    comment=models.TextField()
    post_id=models.IntegerField(default=0)
