from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader

from blog.models import Post

def blog_index(request):
	posts = Post.objects.all()

	## Usando el metodo get_template:
	# template = loader.get_template('blog/blog_index.html')
	## Luego usando la funcion RequestContext
	#context = RequestContext(request, {
	#	'posts':posts,
	#})

	# Usando el shortcut de render:
	context = {'posts':posts}

	# Usando el HttpResponse, el template y el context de RequestContext:
	#return HttpResponse(template.render(context))

	# Usando el shotcut render():
	return render(request, 'blog/blog_index.html', context)

def post_detail(request, post_title):
	# Excepcion 404 usando django.http.Http404:
	#try:
	#	post = Post.objects.get(post_title=post_title)
	#except Post.DoesNotExist:
	#	raise Http404('Este post no existe.')

	# Usando el shortcut get_object_or_404:
	post = get_object_or_404(Post, post_title=post_title)

	response = "Estas buscando el post titulado: %s."
	return HttpResponse(response % post_title)