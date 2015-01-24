from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=140)
	pub_date = models.DateTimeField('date published')
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question)
	answer_text = models.CharField(max_length=200)

	def __unicode__(self):
		return self.answer_text