from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . import methods as api_methods

from twitterApp.models import Profile
from twitterApp.views import set_new_token, see_tweets



# disabling csrf token
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    def post(self, request, index, *args, **kwargs):
        if index != 'tweet' and index != 'login':
            return api_methods.api_method_not_found()
        if index == 'tweet':
            return api_methods.tweet(request)
        if index == 'login':
            return api_methods.login(request)

    def get(self, request, index, *args, **kwargs):
        return api_methods.api_method_not_found()


def get_new_token(request):
    user_profile = Profile.objects.get(user=request.user)
    new_token = api_methods.create_new_access_token(profile=user_profile)
    set_new_token(new_token=new_token)
    return see_tweets(request=request)
