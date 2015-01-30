from django.shortcuts import render

def mimico(request):
	username = request.user.username
	context = {'username': username }
	return render(request, 'scada/mimico.html', context)