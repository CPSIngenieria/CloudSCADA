from django.contrib import admin
from userprofiles.models import Profile

class ProfileAdmin(admin.ModelAdmin):

	fieldsets = [
		( 'User information', { 'fields': ['user'] } ),
		( 'Rol information', { 'fields': ['rol'] } ),
	]

	list_display = ('user', 'rol', 'can_access_scada')
	list_filter = ['rol']
	search_fields = ['user__username']

admin.site.register(Profile, ProfileAdmin)