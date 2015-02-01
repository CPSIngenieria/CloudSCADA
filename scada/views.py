from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required

def access_scada_permission(user):
	return user.has_perm('userprofiles.access_scada')

# @login_required
# @user_passes_test(access_scada_permission)
@permission_required('userprofiles.access_scada', raise_exception=True )
def mimico(request):
	username = request.user.username
	context = {'username': username }
	return render( request, 'scada/mimico.html', context )