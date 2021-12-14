from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login


def login_user(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            uti = authenticate(username=username, password=password)

            if uti:
                if uti.is_active:
                    login(request, uti)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("Your account is disabled.")
        else:
            return render(request, "water_final/login.html", context={"login_error": "用户名或密码错误"})
            # return HttpResponse("用户名或密码错误")

    else:
        return render(request, "water_final/login.html", context={})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
