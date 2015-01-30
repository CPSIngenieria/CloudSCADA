from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from doubts.views import QuestionsViewSet
from blog.views import PostsViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionsViewSet)
router.register(r'posts', PostsViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CloudSCADA.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('cps.urls', namespace="landing")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^faq/', include('doubts.urls', namespace="doubts")),
    url(r'^scada/', include('scada.urls', namespace="scada")),
    url(r'^userprofiles/', include('userprofiles.urls', namespace="userprofiles")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
