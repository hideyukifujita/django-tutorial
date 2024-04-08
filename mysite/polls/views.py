from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    """requestを受け取って、文字列をレンダリングする。
    Args:
        request (HttpRequest): HttpRequestオブジェクト

    Returns:
        HttpResponse: 文字列
    """
    return HttpResponse("Hello, world. You're at the polls index.")