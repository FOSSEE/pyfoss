from django.db import models

class Nav(models.Model):
	"""Main navigation links"""
	nav_name = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	position = models.IntegerField()
	visible = models.BooleanField()

	def __unicode__(self):
		return self.nav_name

class SubNav(models.Model):
	"""Navigation links for pages"""
	nav = models.ForeignKey(Nav)
	subnav_name = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	position = models.IntegerField()
	visible = models.BooleanField()

	def __unicode__(self):
		return self.subnav_name

class Page(models.Model):
	"""Page that will be dispatched"""
	permalink = models.CharField(max_length=200)
	heading = models.CharField(max_length = 500)
	content = models.TextField()
	visible = models.BooleanField()
	pub_date = models.DateTimeField('date published', auto_now_add=True)

	def __unicode__(self):
		return self.heading