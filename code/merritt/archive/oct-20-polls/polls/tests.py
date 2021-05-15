from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuestionModelTest(TestCase):

  def test_was_published_recently_with_future_question(self):
    '''
    was_published_recently returns FALSE for questions whos pub_date is in the future
    '''
    time = timezone.now() + datetime.timedelta(days=30)
    future_question = Question(pub_date=time)
    self.assertIs(future_question.was_published_recently(), False)

  def test_was_published_recently_with_old_question(self):
    '''
    was_published_recently returns FALSE for questions whos pub_date is older than 1 day
    '''
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
    '''
    was_published_recently returns TRUE for questions whos pub_date is within the last day
    '''
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date = time)
    self.assertIs(recent_question.was_published_recently(), True)


def create_question(question_text, days):

  time = timezone.now() + datetime.timedelta(days=days)
  return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTest(TestCase):
  def test_no_questions(self):
    '''
    if no question exist, a message is displayed
    '''
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'No polls are available.')
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_past_question(self):
    '''
    questions with a pub_date in the past are displayed on index.html
    '''
    create_question(question_text='Past question.', days=-30)
    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      ['<Question: Past question.>']
    )

  def test_future_question(self):
    '''
    questions with pub_date in the future are not displayed on the page
    '''
    create_question(question_text='Future question.', days=30)
    response = self.client.get(reverse('polls:index'))
    self.assertContains(response, 'No polls are available.')
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

  def test_future_question_and_past_question(self):
    '''
    even if both past and future questions exist only the past questions are displayed
    '''

    create_question(question_text='Past question.', days=-30)
    create_question(question_text='Future question.', days=30)

    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      ['<Question: Past question.>']
    )

  def test_two_past_questions(self):
    '''
    the questions index page may display multiple questions
    '''

    create_question(question_text='Past question 1.', days=-30)
    create_question(question_text='Past question 2.', days=-5)

    response = self.client.get(reverse('polls:index'))
    self.assertQuerysetEqual(
      response.context['latest_question_list'],
      ['<Question: Past question 2.>', '<Question: Past question 1.>']
    )

class QuestionDetailViewTests(TestCase):
  def test_future_question(self):
    '''
    the detail view of a question with a pub_date in the future returns a 404 not found
    '''
    future_question = create_question(question_text='Future question.', days=5)
    url = reverse('polls:detail', args= (future_question.id,))

    response = self.client.get(url)
    self.assertEqual(response.status_code, 404)

  def test_past_question(self):
    '''
    the detail view of a question with a pub_date in the past displays the questions text
    '''
    past_question = create_question(question_text='Past question.', days=-5)
    url = reverse('polls:detail', args= (past_question.id,))

    response = self.client.get(url)
    self.assertContains(response, past_question.question_text)