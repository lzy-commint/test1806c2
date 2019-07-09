from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    """
    访问首页
    :param request:
    :return:
    """
    return HttpResponse("index")


def login(request):
    """
    访问登录页面
    :param request:
    :return:
    """
    return redirect("/index")
