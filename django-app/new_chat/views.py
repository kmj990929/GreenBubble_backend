from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'new_chat/index.html', {})

def room(request, room_name):
    return render(request, 'new_chat/room.html', {
        'room_name': mark_safe(json.dumps(room_name))
    })
