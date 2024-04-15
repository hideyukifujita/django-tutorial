import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200,  db_comment="質問文")
    pub_data = models.DateTimeField("data published", db_comment="登録日")
    
    def __str__(self):
        """質問文を返す

        Returns:
            str: 質問文
        """
        return self.question_text
    
    def was_published_recently(self):
        """pub_dataが現時刻から一日以内かどうか

        Returns:
            bool: True or False
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, db_comment="QustionとのKey")
    choice_text = models.CharField(max_length=200, db_comment="選択肢")
    votes = models.IntegerField(default=0, db_comment="投票数")

    def __str__(self):
        """選択文を返す
        
        Returns:
            str: 選択文
        """
        return self.choice_text