from django.conf.urls import patterns, url
from userprofiles import views

urlpatterns = patterns('',
	# ejemplo: /userprofiles/
	url(r'^new_user/$', views.new_user, name='new_user'),
	url(r'^login/$', views.user_login, name='user_login'),
	url(r'^logout/$', views.user_logout, name='user_logout'),
)