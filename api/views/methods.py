from django.http import JsonResponse

from django.contrib.auth.hashers import check_password

from api import models as ApiModels
from twitterApp import models as TwitterModels
import secrets as pythonSecrets


def create_new_access_token(profile: TwitterModels.Profile) -> str:
    access_token = ApiModels.ApiAccessToken.objects.get_or_create(user=profile)[0]
    access_token.token = pythonSecrets.token_urlsafe(nbytes=64)
    access_token.save()
    return access_token.token


def user_password_was_incorrect() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "Password was Incorrect",
    })


def token_was_not_found() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "Incorrect Access Token",
    })


def user_profile_not_found() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "User Profile Was Not Found",
    })


def api_method_not_found() -> JsonResponse:
    return JsonResponse(data={
        'ok': False,
        'description': "Method Not Found - For Security Reasons API Methods are only available through POST method",
    })


def get_user(token) -> TwitterModels.Profile:
    try:
        access_token_object = ApiModels.ApiAccessToken.objects.get(token__exact=token)
        profile = access_token_object.user
    except Exception:
        raise Exception
    return profile


def login(request) -> JsonResponse:
    try:
        profile = TwitterModels.Profile.objects.get(user__username__exact=request.POST['username'])
        if not check_password(password=request.POST['password'], encoded=profile.user.password):
            return user_password_was_incorrect()
    except Exception:
        return user_profile_not_found()
    token = create_new_access_token(profile)
    return JsonResponse(data={
        'ok': True,
        'token': token
    })


def return_tweet_request_format():
    return JsonResponse(data={
        'ok': False,
        'description': 'Tweet should have tweet-title & tweet-content and must be requested through POST method'
    })


def tweet(request) -> JsonResponse:
    try:
        profile = get_user(request.POST['token'])
    except Exception:
        return token_was_not_found()
    try:
        tweet = TwitterModels.Tweet(user=profile, name=request.POST['tweet-title'],
                                    content=request.POST['tweet-content'])
    except Exception:
        return return_tweet_request_format()
    tweet.save()
    return JsonResponse(data={
        'ok': True,
        'description': 'Tweet was created successfully'
    })
