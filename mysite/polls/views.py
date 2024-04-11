from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

LATEST_QUESTION_ITEMS = 5
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """最新の5件の質問項目を日付順で返す

        Returns:
            Question: 質問項目
        """
        return Question.objects.order_by("-pub_data")[:LATEST_QUESTION_ITEMS]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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