import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from doubts.models import Question

def create_question(question_text, days):
	"""
	Esta funcion crea una pregunta con un question_text y una pub_date
	determinada por la cantidad de dias de offset en days.
	"""
	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(TestCase):

	def test_index_view_with_no_questions(self):
		"""
		Si no existen preguntas, debe dar un mensaje apropiado.
		"""
		response = self.client.get(reverse('doubts:doubts'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No existen preguntas aun en el FAQ")
		self.assertQuerysetEqual(response.context['questions'], [])

	def test_index_view_with_a_past_question(self):
		"""
		La vista con una pregunta cuya pub_date sea del pasado deberia mostrarla.
		"""
		create_question(question_text="Past question", days=-30)
		response = self.client.get(reverse('doubts:doubts'))
		self.assertQuerysetEqual(response.context['questions'], ['<Question: Past question>'])

	def test_index_view_with_a_future_question(self):
		"""
		La vista no deberia mostrar preguntas cuya pub_date sea en el futuro.
		"""
		create_question(question_text="Future question", days=30)
		response = self.client.get(reverse('doubts:doubts'))
		self.assertQuerysetEqual(response.context['questions'], [])
		self.assertContains(response, "No existen preguntas aun en el FAQ", status_code=200)

	def test_index_view_with_future_and_past_questions(self):
		create_question(question_text="Future question", days=30)
		create_question(question_text="Past question", days=-30)
		response = self.client.get(reverse('doubts:doubts'))
		self.assertQuerysetEqual(response.context['questions'], ['<Question: Past question>'])

	def test_index_view_with_two_past_questions(self):
		create_question(question_text="Past question 1", days=-30)
		create_question(question_text="Past question 2", days=-5)
		response = self.client.get(reverse('doubts:doubts'))
		self.assertQuerysetEqual(
			response.context['questions'], 
			['<Question: Past question 2>', '<Question: Past question 1>']
		)

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