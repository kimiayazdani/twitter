from django.urls import path
from twitterApp import views

app_name = 'twitterApp'

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.register_user, name='register'),
    path('tweet/', views.add_tweet, name='tweet'),
    path('login_req/', views.redirect_to_login)
]
