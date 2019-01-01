from django.contrib import admin
from twitterApp.models import Profile, Tweet,RequestLog

admin.site.register(Profile)
admin.site.register(Tweet)
admin.site.register(RequestLog)

