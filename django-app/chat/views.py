# chat/views.py
from django.shortcuts import render,redirect
from django.utils.safestring import mark_safe
import json

def index(request):
    if 'user_name' in request.session.keys():
        return render(request, 'chat/index.html', {})
    else:
        return redirect('user_signin')

def room(request, room_name):
    if 'user_name' in request.session.keys():
        return render(request, 'chat/room.html', {
            'room_name': mark_safe(json.dumps(room_name))
            })
    else:
        return redirect('user_signin')
