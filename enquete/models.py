import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date de publication')
    def __str__(self):
        return self.question_text

    def a_ete_pub_recemment(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) 


class Choix(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text


