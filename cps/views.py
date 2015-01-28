from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User



def landing(request):

	context = {'saludo':'Hola CPS!'}
	return render(request, 'cps/landing.html', context)

def new_user(request):

	username = request.POST['username']
	password1 = request.POST['password1']
	password2 = request.POST['password2']
	email = request.POST['email']

	# Verificamos que no exista un usuario con ese username:
	try:
		User.objects.get(username=username)
	except User.DoesNotExist:
		valid_username = username
	else:
		context = {
			'error_message': "Ya existe un usuario con ese username. Por favor selecciona uno diferente",
		}
		return render(request, 'cps/landing.html', context)

	# Verificamos que no exista un usuario con ese email:
	try:
		User.objects.get(email=email)
	except User.DoesNotExist:
		valid_email = email
	else:
		context = {
			'error_message': "Ya existe un usuario con ese email. Por favor selecciona uno diferente",
		}
		return render(request, 'cps/landing.html', context)

	# Verificamos que los dos passwords sean iguales
	if password1 and password2 and password1 != password2:
		context = {
			'error_message': "Los passwords no coinciden. Por favor intente de nuevo",
		}
		return render(request, 'cps/landing.html', context)		
	else:
		valid_password = password2
		
	User.objects.create_user(valid_username,valid_email,valid_password)
	return HttpResponseRedirect(reverse('landing:landing'))

	