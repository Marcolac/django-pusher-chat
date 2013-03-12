from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
import pusher

pusher.app_id = settings.PUSHER_APP_ID
pusher.key = settings.PUSHER_KEY
pusher.secret = settings.PUSHER_SECRET

p = pusher.Pusher()

def message(request):
    if request.method == 'GET':
        p['chat'].trigger('message', {
            'val': request.GET.get('val'),
            'name': request.GET.get('name'),
        })

    return HttpResponse('blabla', content_type="text/javascript")