from django.shortcuts import render


def landing(request):

	context = {'saludo':'Hola CPS!'}
	return render(request, 'cps/landing.html', context)