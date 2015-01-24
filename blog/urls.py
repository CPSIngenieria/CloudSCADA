from django.conf.urls import patterns, url
from blog import views 

urlpatterns = patterns('',
	# ejemplo: /blog/
	url(r'^$', views.blog_index, name='blog_index'),
	# ejemplo: /blog/CPS-is-on/
	url(r'^(?P<post_title>\w+)/$', views.post_detail, name='post_detail'),
)