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


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     print("I AM HERE ------------------")
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print("I AM EVEN HERE!!!!!!!!!!!!!!!!!!!!!!")
#     instance.profile.save()
#     # pass
