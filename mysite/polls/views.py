from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    """requestを受け取って、最新の5件の質問項目をカンマで区切り、日付順で表示する。

    Args:
        request (HttpRequest): HttpRequestオブジェクト

    Returns:
        HttpResponse: 文字列
    """
    latest_question_list = Question.objects.order_by("-pub_data")[:5]
    output  = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

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