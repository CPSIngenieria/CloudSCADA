from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def landing(request):

	username = request.user.username
	
	if not username:
		username = "invitado" 
	
	context = { 'active_user': username }
	return render(request, 'cps/landing.html', context)

