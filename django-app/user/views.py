from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from .serializers import UserSerializer

def index(request):
    if 'user_name' in request.session.keys():
        response = {'loginSuccess':True}
        response['username'] = request.session['user_name']
        response['useremail'] = request.session['user_email']
        return JsonResponse(response, safe=False, status = 200)
    else:
        return redirect('user_signin')

def signup(request):
    return render(request, 'user/signup.html')

def join(request):
    print(request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name = name, user_email = email, user_password = pw)
    user.save()
    return redirect('user_signin')

def verify(request):
    user = User.objects.get(id=request.COOKIES.get('user_id'))
    user.save()
    response = redirect('user_index')
    response.delete_cookie('user_id')
    request.session['user_name'] = user.user_name
    request.session['user_email'] = user.user_email
    return response

def signin(request):
    return render(request, 'user/signin.html')

def login(request):
    loginEmail = request.POST['loginEmail']
    loginPW = request.POST['loginPW']
    try:
        user = User.objects.get(user_email = loginEmail)
    except:
        return redirect('user_loginFail')
    if user.user_password == loginPW:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('user_index')
    else:
        return redirect('user_loginFail')

def logout(request):
    del request.session['user_name']
    del request.session['user_email']
    return redirect('user_signin')

def loginFail(request):
    return render(request, 'user/loginFail.html')

def forgetpw(request):
    return render(request, 'user/forgetpw.html')

def findpw(request):
    inputEmail = request.POST['inputEmail']
    try:
        user = User.objects.get(user_email = inputEmail)
    except:
        return redirect('user_findpwFail')
    request.session['user_name'] = user.user_name
    request.session['user_email'] = user.user_email
    return redirect('user_viewpw')

def findpwFail(request):
    return render(request, 'user/findpwFail.html')

def viewpw(request):
    name = request.session['user_name']
    user = User.objects.get(user_name = name)
    content = {'password' : user.user_password}
    return render(request, 'user/viewpw.html', content)

class Test_user(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
