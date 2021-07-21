from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Choice, Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]#descending pub_date
    context = {
        'latest_question_list':latest_question_list
    }
    return render(request, 'polls/index.html', context)
#we will have 4 views in this page
#index page
#detail with text of questions
#vote
#results
def detail(request, question_id):#as many pages as questions in DB
    question= get_object_or_404(Question, pk=question_id)
    #pk stands for primary key, the unique non-repeating key is for the data
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = f'you are looking at the results of question {question_id}'
    return HttpResponse(response)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])#everything you send in a form is put into a dictionary by django. You can access it through request.post
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You did not select a choice.",
        })
    selected_choice.votes +=1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=[question.id]))#a tuple with one item in it needs a trailing comma