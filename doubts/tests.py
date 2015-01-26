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

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() deberia retornar False para preguntas
		cuya pub_date sea mas vieja que 1 dia.
		"""
		old_time = timezone.now() - datetime.timedelta(days=30)
		old_question = Question(pub_date=old_time)
		self.assertEqual(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() deberia retornar True para preguntas
		cuya pub_date sea no mas de 1 dia hacia atras.
		"""
		recent_time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date=recent_time)
		self.assertEqual(recent_question.was_published_recently(), True)