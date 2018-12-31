from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . import methods as api_methods


# disabling csrf token
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    def post(self, request, index, *args, **kwargs):
        if index != 'tweet':
            return api_methods.api_method_not_found()
        return api_methods.tweet(request)

    def get(self, request, index, *args, **kwargs):
        return api_methods.api_method_not_found()
