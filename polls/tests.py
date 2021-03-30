from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

import datetime


def create_question(question_text, days_offset_from_now):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """

    question_date = timezone.now() + datetime.timedelta(days=days_offset_from_now)
    return Question.objects.create(question_text=question_text, pub_date=question_date)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['recent_five_questions'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """

        create_question(question_text="Past Question.",
                        days_offset_from_now=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['recent_five_questions'], [
                '<Question: Past Question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on the
        index page
        """

        create_question(question_text="Future Question.",
                        days_offset_from_now=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")

        self.assertQuerysetEqual(response.context['recent_five_questions'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions should
        be displayed
        """

        create_question(question_text="Past question.",
                        days_offset_from_now=-30)
        create_question(question_text="Future question.",
                        days_offset_from_now=30)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['recent_five_questions'], [
                '<Question: Past question.>']
        )

    def test_past_two_questions(self):
        """
        The questions index page should display multiple questions
        """

        create_question(question_text="Past question 1",
                        days_offset_from_now=-30)
        create_question(question_text="Past question 2",
                        days_offset_from_now=-5)

        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['recent_five_questions'], [
                '<Question: Past question 2>', '<Question: Past question 1>']
        )


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose 
        pub_date is in the future
        """

        date_of_one_month_from_now = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=date_of_one_month_from_now)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose pub_date
        is older than 1 day.
        """

        date_before_one_day_from_now = timezone.now(
        ) - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=date_before_one_day_from_now)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose pub_date
        is within the last day
        """

        date_of_last_day = timezone.now() - datetime.timedelta(hours=23,
                                                               minutes=59, seconds=59)
        recent_question = Question(pub_date=date_of_last_day)
        self.assertIs(recent_question.was_published_recently(), True)
