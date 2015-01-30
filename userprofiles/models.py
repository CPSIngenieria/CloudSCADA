from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

	user = models.OneToOneField(User)
	rol = models.CharField(max_length=200)

	class Meta:
		permissions = (
			('access_scada','Can access the SCADA'),
		)

	def __unicode__(self):
		return self.user.username + ' - ' + self.rol

	def can_access_scada(self):
		return self.user.has_perm('userprofiles.access_scada')
