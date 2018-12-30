from twitterApp.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    print(response)
    print(user)
    Profile.objects.create(user=user)
