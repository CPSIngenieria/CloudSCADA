import mandrill
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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
			'signin_error_message': "Ya existe un usuario con ese username. Por favor selecciona uno diferente",
		}
		return render(request, 'cps/landing.html', context)

	# Verificamos que no exista un usuario con ese email:
	try:
		User.objects.get(email=email)
	except User.DoesNotExist:
		valid_email = email
	else:
		context = {
			'signin_error_message': "Ya existe un usuario con ese email. Por favor selecciona uno diferente",
		}
		return render(request, 'cps/landing.html', context)

	# Verificamos que los dos passwords sean iguales
	if password1 and password2 and password1 != password2:
		context = {
			'signin_error_message': "Los passwords no coinciden. Por favor intente de nuevo",
		}
		return render(request, 'cps/landing.html', context)		
	else:
		valid_password = password2
		
	User.objects.create_user(valid_username,valid_email,valid_password)

	# Enviamos un correo electronico con la informacion de signup:
	try:
		mandrill_client = mandrill.Mandrill('_SoGpYeWNJ0p3ziJ1Hn75g')
		template_content = [{'content':valid_username, 'name':'usuario'}]
		message = {
			'to':[
				{
					'email': valid_email,
					'name': valid_username,
					'type': 'to'
				}
			],
			'merge_language':'handlebars',
			'from_email':'andres@cpsingenieria.co',
			'merge_vars':[
				{
					'rcpt':valid_email,
					'vars':[{'content':valid_username, 'name':'usuario'},{'content':valid_password, 'name':'clave'}]
				}
			]
		}
		result = mandrill_client.messages.send_template(template_name='first_test', 
			template_content=template_content, message=message, async=False)
	except mandrill.Error, e:
		print 'A mandrill error occurred: %s - %s' % (e.__class__, e)

	return HttpResponseRedirect(reverse('landing:landing'))

def user_login(request):

	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user is not None:
		# Se verifico el password para el usuario especificado.
		if user.is_active:
			# El usuario esta activo:
			login(request, user)
			return HttpResponseRedirect(reverse('landing:landing'))
		else: 
			# El usuario no esta activo
			context = {
				'login_error_message':"Lo sentimos, su cuenta no esta activa.",
			}
			return render(request, 'cps/landing.html', context)
	else:
		# EL sistema de autenticacion no fue capaz de autenticar al usuario:
		context = {
				'login_error_message':"Usuario o contrasena incorrectas",
			}
		return render(request, 'cps/landing.html', context)

def user_logout(request):

	logout(request)
	return HttpResponseRedirect(reverse('landing:landing'))
