from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
    """requestを受け取って、最新の5件の質問項目を日付順でHTMLに表示する。

    Args:
        request (HttpRequest): HttpRequestオブジェクト

    Returns:
        HttpResponse: HTML
    """
    latest_question_list = Question.objects.order_by("-pub_data")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    """request, question_idを受け取り、detail.htmlを表示

    Args:
        request (HttpRequest): HttpRequestオブジェクト
        question_id (int): 質問のid

    Returns:
        HttpResponse: HTML
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

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