import datetime#import things from the python standard library first then import third party libraries next
#separate with a blank line

from django.db import models
from django.utils import timezone

# Create your models here.
#question model
class Question(models.Model):
    question_text=models.CharField(max_length=200)#basically a character field is a string with a maximum length
    pub_date=models.DateTimeField()#publication date allows for ordering, latest questions first, etc.

    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days=1)#was this published within the last 24 hours? now minus 1 day
        
    def __str__(self):
        return self.question_text

#choice model
class Choice(models.Model):
    #if a a question goes awary, the question goes away with the on_delete
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #what question it is an answer to so Django can do a reverse lookup, choices are subordinate to questions
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)#keep track of the number of votes by choice

    def __str__(self):
        return self.choice_text
