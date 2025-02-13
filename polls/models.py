import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self): 
        return self.question_text
    
    def total_votes(self):
        return self.choice_set.aggregate(models.Sum('votes'))['votes__sum'] or 0

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def has_votes(self):
        return self.choice_set.filter(votes__gt=0).exists()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self): 
        return self.choice_text
