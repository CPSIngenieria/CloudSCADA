from django.http import HttpResponse
from django.shortcuts import render

def blog_index(request):
	return HttpResponse('Indice del blog :)')

def post_detail(request, post_title):
	response = "Estas buscando el post titulado: %s."
	return HttpResponse(response % post_title)