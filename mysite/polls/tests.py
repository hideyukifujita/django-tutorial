import datetime

from django.test import TestCase
from django.utils import timezone

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