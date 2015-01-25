from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CloudSCADA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^faq/', include('doubts.urls', namespace="doubts")),
    url(r'^admin/', include(admin.site.urls)),
)
