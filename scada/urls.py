from django.conf.urls import patterns, url 
from scada import views

urlpatterns = patterns('',
	# ejemplo: /scada/
	url(r'^mimico/$', views.mimico, name='mimico')
)