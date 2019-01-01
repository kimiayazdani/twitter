from django.contrib.sessions.models import Session
from . import methods
from django.http import HttpResponseForbidden, HttpResponse

time_range = 1000000
max_requests_count_in_time_range = 20000

max_bad_requests_count = 20000


class HandleMiddleware:
    def __init__(self, get_response, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.get_response = get_response

    def __call__(self, request):

        req_log = methods.monitor_request(request)
        count = methods.count_recent_requests(request_log=req_log, time_range=time_range)
        if count >= max_requests_count_in_time_range:
            return HttpResponseForbidden(HttpResponse("Too Many Requests in a very short time dude"))

        if request.user.is_authenticated:
            stored_session_key = request.user.logged_in_user.session_key

            if stored_session_key and stored_session_key != request.session.session_key:
                Session.objects.get(session_key=stored_session_key).delete()

            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()

        try:
            response = self.get_response(request, *self.args, **self.kwargs)

            if not 199 < response.status_code < 300:
                req_log.allowed_request = False
                req_log.save()
                bad_requests_count = methods.count_bad_requests(request_log=req_log)

                if bad_requests_count > max_bad_requests_count:
                    return HttpResponseForbidden(HttpResponse("Dude too many unallowed requests ... "))

            return response

        except:

            # kim inja mishe
            print('shit')
