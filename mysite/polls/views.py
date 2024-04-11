from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

LATEST_QUESTION_ITEMS = 5
def index(request):
    """requestを受け取って、最新の5件の質問項目を日付順でHTMLに表示する

    Args:
        request (HttpRequest): HttpRequestオブジェクト

    Returns:
        HttpResponse: HTML
    """
    latest_question_list = Question.objects.order_by("-pub_data")[:LATEST_QUESTION_ITEMS]
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
    """request, question_idを受け取り、results.htmlを表示

    Args:
        request (HttpRequest): HttpRequestオブジェクト
        question_id (int): 質問のid

    Returns:
        HttpResponse: HTML
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

ADD_VOTES = 1
def vote(request, question_id):
    """request, question_idを受け取り、選択肢の投票数に+1し、results.htmlにリダイレクトする

    Args:
        request (HttpRequest): HttpRequestオブジェクト
        question_id (int): 質問のid
        
    Returns:
        HttpResponseRedirect: HTML
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + ADD_VOTES
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))