from django.db import models

class Post(models.Model):
	post_title = models.CharField(max_length=140)
	pub_date = models.DateTimeField('date published')
	tag = models.CharField(max_length=50)
	views = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.post_title