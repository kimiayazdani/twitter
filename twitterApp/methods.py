import datetime


def get_client_ip(request):
    request_info = {}
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    request_info['ip'] = ip
    request_info['browser'] = request.META['HTTP_USER_AGENT']
    request_info['time'] = datetime.datetime.now()
    return request_info
    # check the format: request_info['time'] = datetime.datetime.now().strftime('%H:%M:%S')
