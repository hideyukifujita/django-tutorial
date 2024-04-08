from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    """request, question_idを受け取り、文字列を返す

    Args:
        request (HttpRequest): HttpRequestオブジェクト
        question_id (int): 質問のid

    Returns:
        HttpResponse: 文字列
    """
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    """request, question_idを受け取り、文字列を返す

    Args:
        request (HttpRequest): HttpRequestオブジェクト
        question_id (int): 質問のid

    Returns:
        HttpResponse: 文字列
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    """request, question_idを受け取り、文字列を返す

    Args:
        request (HttpRequest): HttpRequestオブジェクト
        question_id (int): 質問のid

    Returns:
        HttpResponse: 文字列
    """
    return HttpResponse("You're voting on question %s." % question_id)