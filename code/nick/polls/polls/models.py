from django.db import models

# Create your models here.
#question model
class Question(models.Model):
    question_text=models.CharField(max_length=200)#basically a character field is a string with a maximum length
    pub_date=models.DateTimeField()#publication date allows for ordering, latest questions first, etc.
#choice model
class Choice(models.Model):
    #if a a question goes awary, the question goes away with the on_delete
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #what question it is an answer to so Django can do a reverse lookup, choices are subordinate to questions
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)#keep track of the number of votes by choice
