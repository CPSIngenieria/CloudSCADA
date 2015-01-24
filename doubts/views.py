from django.http import HttpResponse
from django.shortcuts import render

def doubts(request):
	return HttpResponse("Aca van las preguntas comunes :)")
