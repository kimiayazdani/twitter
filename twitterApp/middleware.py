from django.contrib.sessions.models import Session


class HandleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # vahiiid inja ghable request ha ejra mishe =)
        if request.user.is_authenticated:
            stored_session_key = request.user.logged_in_user.session_key

            if stored_session_key and stored_session_key != request.session.session_key:
                Session.objects.get(session_key=stored_session_key).delete()

            request.user.logged_in_user.session_key = request.session.session_key
            request.user.logged_in_user.save()

        response = self.get_response(request)

        return response
