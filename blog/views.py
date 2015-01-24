from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from blog.models import Post

def blog_index(request):
	posts = Post.objects.all()
	template = loader.get_template('blog/blog_index.html')
	context = RequestContext(request, {
		'posts':posts,
	})
	return HttpResponse(template.render(context))

def post_detail(request, post_title):
	response = "Estas buscando el post titulado: %s."
	return HttpResponse(response % post_title)