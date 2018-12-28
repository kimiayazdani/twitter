from django.db import models
from django.contrib.auth.models import User

from twitter import settings


class TwitterUser(User):
    # user = models.OneToOneField(User, related_name='TwitterUser', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', blank=True)


    def __str__(self):
        return self.username


class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.name + " " + self.content

