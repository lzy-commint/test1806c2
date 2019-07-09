from django.http import HttpResponse


def index(request):
    """
    访问首页
    :param request:
    :return:
    """
    return HttpResponse("index")
