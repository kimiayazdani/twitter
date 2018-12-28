from django.shortcuts import render
from twitterApp.forms import RegistrationForm
from twitterApp.models import Tweet, TwitterUser

from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

import random


def register_user(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return see_tweets(request)
    return render(request=request, template_name='registration.html',
                  context={'form': form})


@login_required(login_url='/v1/login')
def twit(request):
    return render(request=request, template_name='twits.html')


def user_login(request, dng=None, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username + " " + password)
        user = TwitterUser.objects.get(username=username, password=password)
        if user:
            login(request, user, backend)
            return HttpResponseRedirect(reverse('home'))
        else:
            return user_login(request, "Wrong username or password")
    return render(request=request, template_name='login.html', context={'danger': dng})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def redirect_to_login(request):
    return user_login(request, "Login is required for this section.")


@login_required(login_url="/v1/login")
def add_tweet(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        content = request.POST.get("content")
        print(request.user.username)
        user = TwitterUser.objects.get(username=request.user.username)
        t = Tweet.objects.get_or_create(user=user, name=name, content=content)[0]
        t.save()
        return see_tweets(request)
    return render(request=request, template_name='twits.html')


def see_tweets(request):
    things = list(Tweet.objects.all())
    print(things.reverse())
    colors = ["success", "info", "danger", "warning", "default"]
    return render(request=request, template_name='view_tweets.html',
                  context={"things": things, "color": str("tweet tweet-" + random.choice(colors))})
