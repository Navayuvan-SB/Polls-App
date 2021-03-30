from django.test import TestCase
from django.utils import timezone

from .models import Question

import datetime


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose 
        pub_date is in the future
        """

        date_of_one_month_from_now = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=date_of_one_month_from_now)
        self.assertIs(future_question.was_published_recently(), False)
