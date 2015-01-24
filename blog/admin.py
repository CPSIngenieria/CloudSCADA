from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):

	fieldsets = [
		(None, { 'fields': ['post_title','tag','views'] } ),
		('Date information', { 'fields': ['pub_date'], 'classes': ['collapse'] } ),
	]

	list_display = ('post_title', 'pub_date', 'tag', 'views')

	list_filter = ['pub_date', 'tag']

	search_fields = ['post_title']

admin.site.register(Post, PostAdmin)	