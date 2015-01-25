from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone

from doubts.models import Question

def doubts(request):

	questions = Question.objects.all()
	context = {'questions':questions}
	return render(request, 'doubts/doubts.html', context)

def new_doubt(request):

	questions = Question.objects.all()
	new_question = request.POST['question']

	if not new_question:
		context = {'questions':questions, 'error_message':"Debes escribir una pregunta!"}
		return render(request, 'doubts/doubts.html', context)
	else:
		new_question_recieved = Question(question_text=new_question, pub_date=timezone.now())
		new_question_recieved.save()
		return HttpResponseRedirect(reverse('doubts:doubts'))