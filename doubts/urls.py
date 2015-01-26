from django.conf.urls import patterns, url
from doubts import views

urlpatterns = patterns('',
	# ejemplo: /doubts/
	url(r'^$', views.doubts, name='doubts'),
	url(r'^new_doubt/$', views.new_doubt, name='new_doubt')
)