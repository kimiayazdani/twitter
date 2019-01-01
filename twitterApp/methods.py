from datetime import timedelta
from twitterApp import models as twitter_models


def get_request_info(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip, request.META['HTTP_USER_AGENT']


def monitor_request(request, *args, **kwargs):
    ip, user_agent = get_request_info(request)
    request_log = twitter_models.RequestLog(ip=ip, user_agent=user_agent)
    request_log.save()
    return request_log


def count_recent_requests(request_log, time_range):
    try:
        time_thing = request_log.time_stamp - timedelta(microseconds=time_range)
        reqs = twitter_models.RequestLog.objects.all().filter(time_stamp__gte=time_thing)
        return reqs.count()
    except:
        return 0


def count_bad_requests(request_log):
    try:
        reqs = twitter_models.RequestLog.objects.all().filter(allowed_request=False)
        return reqs.count()
    except:
        return 0
