from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from . import methods as apiMethods


# disabling csrf token
# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    def post(self, req, index, *args, **kwargs):
        return JsonResponse(data={'req': str(req.method + index)})

    def get(self, req, index, *args, **kwargs):
        return HttpResponse("salam")

    @staticmethod
    def switch_post_index(index, request):
        if index == 'login':
            response = apiMethods.login(request)
        elif index == 'tweet':
            response = apiMethods.tweet(request)
