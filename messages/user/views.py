from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from user import models, forms
from django.contrib.auth.models import User
import logging

logging.basicConfig(level=logging.INFO)


def require(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(request.user.username)
        if user is not None:
            logging.info("login success")
            login(request, user)
            return HttpResponseRedirect('/online/')
        else:
            logging.info("login failed")
            form.add_error('username', "用户名或密码错误")
            return render(request, 'login.html', {'form': form})
    else:
        logging.info("try to login")
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def userlist(request):
    userlist = models.User().get_all()
    return render(request, 'userlist.html', {'users': userlist})

# 删除用户
@login_required
def del_user(request):
    models.User.del_user(request.GET.get('id'))
    User.objects.filter(username=request.GET.get('id'))[0].delete()
    return HttpResponseRedirect('/user/list/')


# 用户注册
def register(request):
    if request.method == 'POST':
        form = forms.UserAdd(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password0')
            label = form.cleaned_data.get('label')
            models.User.add_user(username=username,passwd=password, label=label)
            User.objects.create_user(username=username,password=password)
            return HttpResponseRedirect('/online/')
        else:
            form.add_error("password1", "密码不一致或用户已存在，请重新输入")
            return render(request, 'useradd.html', {"form": form})
    else:
        form = forms.UserAdd()
        return render(request, 'useradd.html', {"form": form})


# 退出登陆
def Mylogout(request):
    logout(request)
    return HttpResponseRedirect('/user/login/')
