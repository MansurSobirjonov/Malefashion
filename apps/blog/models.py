from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts')
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='author')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
