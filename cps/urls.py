from django.conf.urls import patterns, url
from cps import views

urlpatterns = patterns('',
	# ejemplo: /
	url(r'^$', views.landing, name='landing'),
	url(r'^new_user/$', views.new_user, name='new_user')
)