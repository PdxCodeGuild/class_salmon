from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]#descending pub_date
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
    question= get_object_or_404(Question.objects.filter(pub_date__lte=timezone.now()), pk=question_id)#lte is less than or equal to
    #pk stands for primary key, the unique non-repeating key is for the data
    return render(request, 'polls/detail.html', {'question': question})
#on the view level the detail function and the results function are doing the same thing. The only difference to us is the display of options versus results.
def results(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])#everything you send in a form is put into a dictionary by django. You can access it through request.post
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You did not select a choice.",
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=[question.id]))#a tuple with one item in it needs a trailing comma