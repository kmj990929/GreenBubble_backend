from django.urls import path
from . import views

urlpatterns = [
    path('', views.friends_list, name='main_friends_list'),
    path('chat_list',views.chat_list, name='main_chat_list'),
    path('setting', views.setting, name='main_setting'),
]

