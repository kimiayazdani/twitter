from django.shortcuts import render
from twitterApp.forms import UserForm, ProfileForm, LoginWithCaptcha
from twitterApp.models import Tweet, Profile
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.core.mail import send_mail

import random

access_token = "Not refreshed!"


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        prof_form = ProfileForm(data=request.POST, files=request.FILES)
        if user_form.is_valid() and prof_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = prof_form.save(commit=False)
            profile.user = user
            login(request, user, 'django.contrib.auth.backends.ModelBackend')
            if 'avatar' in request.POST:
                profile.avatar = request.POST['avatar']
            try:
                profile.save()
            except:
                pass

            return see_tweets(request)

    user_form = UserForm()
    prof_form = ProfileForm()
    return render(request=request, template_name='registration.html',
                  context={'user_form': user_form, 'prof_form': prof_form, "tkn": access_token})


@login_required(login_url='/v/login')
def twit(request):
    return render(request=request, template_name='twits.html', context={"tkn": access_token})


def user_login(request, dng=None, backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user, backend)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('twitterApp:login'))
    return render(request=request, template_name='login.html', context={'danger': dng, "tkn": access_token})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def redirect_to_login(request):
    return user_login(request, "Login is required for this section.")


@login_required(login_url="/v/login")
def add_tweet(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        content = request.POST.get("content")
        print(request.user.username)
        user = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user)
        t = Tweet.objects.get_or_create(user=user_profile, name=name, content=content)[0]
        t.save()
        return see_tweets(request)
    return render(request=request, template_name='twits.html', context={"tkn": access_token})


def see_tweets(request):
    things = list(Tweet.objects.all())
    print(things.reverse())
    colors = ["success", "info", "danger", "warning", "default"]
    return render(request=request, template_name='view_tweets.html',
                  context={"things": things, "color": str("tweet tweet-" + random.choice(colors)), "tkn": access_token})


def edit_profile(request):
    return render(request=request, template_name='edit_profile.html', context={'img': 'media/hello'})

    user_form = UserForm()
    prof_form = ProfileForm()
    return render(request=request, template_name='registration.html',
                  context={'user_form': user_form, 'prof_form': prof_form})


def set_new_token(new_token):
    global access_token
    access_token = new_token


def login_captcha(request):
    if request.method == 'POST':
        form = LoginWithCaptcha(request.POST)
        if form.is_valid():
            human = True
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            # send_mail(
            #     subject='TWITTER LOGIN WARNING',
            #     message='There were too many attempts for logging in from your account.',
            #     from_email='yazdanikimia@gmail.com',
            #     recipient_list=[user.email]
            # )
            if user:
                login(request, user, backend)
                return HttpResponseRedirect(reverse('home'))
            else:
                return login_captcha(request)
    form = LoginWithCaptcha()

    return render(request=request, template_name='login_captcha.html', context={'tkn': access_token, 'captcha': form})


