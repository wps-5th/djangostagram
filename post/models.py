from django.contrib.auth import get_user_model
from django.db import models


user = get_user_model

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    author = models.ForeignKey(user)
    photo = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(
        user,
        related_name='like_user'
    )
    tags = models.ManyToManyField('Tag')


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(user)
    created_date = models.DateTimeField(auto_now_add=True)

class PostLike(models.Model):
    pass

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return 'Tag({})'.format(self.name)
