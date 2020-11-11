from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('signup', views.signup, name='user_signup'),
    path('signup/join', views.join, name='user_join'),
    path('signin', views.signin, name='user_signin'),
    path('signin/login', views.login, name='user_login'),
    path('loginFail', views.loginFail, name='user_loginFail'),
    path('verify', views.verify, name='user_verify'),
    path('logout', views.logout, name='user_logout'),
    path('forgetpw', views.forgetpw, name='user_forgetpw'),
    path('forgetpw/findpw', views.findpw, name='user_findpw'),
    path('findpwFail', views.findpwFail, name='user_findpwFail'),
    path('forgetpw/viewpw', views.viewpw, name='user_viewpw'),

    path('usersignup', views.Test_user.as_view(), name = 'test_user_view'),
]
