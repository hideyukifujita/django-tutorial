import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuesitonModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """未来の質問に対して、was_published_recently関数がFalseになるか確認
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_data=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_old_question(self):
        """一日経過した質問に対して、was_published_recently関数がFalseになるか確認
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_queston = Question(pub_data=time)
        self.assertIs(old_queston.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """一日以内の質問に対して、was_published_recently関数がTrueになるか確認
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_quesion = Question(pub_data=time)
        self.assertIs(recent_quesion.was_published_recently(), True)


def create_question(question_text, days):
    """question_text, daysを受け取り、Questionを生成して返す

    Args:
        question_text (str): 質問文
        days (int): 日数

    Returns:
        _Question: 質問
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_data=time)


class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """質問がない時の表示を確認
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """過去の質問の表示を確認
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """未来の質問の表示を確認
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """未来と過去の質問の両方の表示を確認
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_question(self):
        """過去の質問を２個生成し、表示を確認
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1]
        )