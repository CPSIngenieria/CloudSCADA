import datetime
from django.test import TestCase
from django.utils import timezone

from doubts.models import Question

class QuestionMethodTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() deberia retornar False para las preguntas
		cuya pub_date sea en el futuro
		"""
		future_time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=future_time)
		self.assertEqual(future_question.was_published_recently(), False) 