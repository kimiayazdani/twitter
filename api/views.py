from django.shortcuts import render
from django.http import JsonResponse,Http404
# Create your views here.
def v1_index(req):

    return JsonResponse( data={'req':str(req)})

def v2_index(req):
    return JsonResponse( data={'req':str(req)})


def v1_login(req):
    try:
        token = req.POST['token']
    except:
        raise Http404
    return JsonResponse(data={})