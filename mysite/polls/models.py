import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField("data published")
    
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
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """選択文を返す
        
        Returns:
            str: 選択文
        """
        return self.choice_text