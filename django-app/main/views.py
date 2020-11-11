from django.shortcuts import render,redirect
from .models import *

from rest_framework.generics import ListAPIView

# Create your views here.
def friends_list(request):
    return render(request, 'main/friends_list.html')

def chat_list(request):
    return render(request, 'main/chat_list.html')

def setting(request):
    return render(request, 'main/setting.html')
