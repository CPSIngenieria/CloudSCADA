from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def landing(request):

	username = request.user.username
	
	if not username:
		username = "invitado" 
	
	context = { 'active_user': username }
	return render(request, 'cps/landing.html', context)