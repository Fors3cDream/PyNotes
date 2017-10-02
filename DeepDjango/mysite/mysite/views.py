from django.http import HttpResponse, Http404
import datetime

def Hello(request):
    return HttpResponse('Hello Django!')

def current_datetime(request):
    now = datetime.datetime.now()
    html = 'It is now %s.' % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)

    html = 'In %s hour(s), it will be %s.' % (offset, dt)

    return HttpResponse(html)