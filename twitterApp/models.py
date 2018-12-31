from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __str__(self):
        return self.user.username + " " + self.user.password


class Tweet(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.name + " " + self.content
