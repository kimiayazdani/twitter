from django.db import models
from twitterApp.models import Profile


# Create your models here.


class ApiAccessToken(models.Model):
    user = models.OneToOneField(to=Profile, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
