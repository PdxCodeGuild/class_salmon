import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_pass_question(self):
        question = create_question("Past Question.", -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        question = create_question("Future Question.", 30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_and_past_question(self):
        future_question = create_question("Future Question.", 30)
        past_question = create_question("Past Question.", -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])

    def test_two_past_questions(self):
        q1 = create_question("Past Question 1.", -30)
        q2 = create_question("Past Question 2.", -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [q2, q1])


class DetailViewTest(TestCase):
    def test_future_question(self):
        q = create_question("Future Question.", 5)
        url = reverse('polls:detail', args=[q.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        q = create_question("Past Question.", -5)
        url = reverse('polls:detail', args=[q.id])
        response = self.client.get(url)
        self.assertContains(response, q.question_text)

