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

class Block(models.Model):
	block_name = models.CharField(max_length=200)
	visible = models.BooleanField()

	def __unicode__(self):
		return self.block_name

class LinkBox(models.Model):
	block = models.ForeignKey(Block)
	linkbox_name = models.CharField(max_length=200)
	position = models.IntegerField()
	visible = models.BooleanField()

	def __unicode__(self):
		return self.linkbox_name

class Link(models.Model):
	linkbox = models.ForeignKey(LinkBox)
	link_name = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	position = models.IntegerField()
	visible = models.BooleanField()

	def __unicode__(self):
		return	self.link_name

class TextBox(models.Model):
	block = models.ForeignKey(Block)
	textbox_name = models.CharField(max_length=200)
	content = models.TextField()
	position = models.IntegerField()
	visible = models.BooleanField()

	def __unicode__(self):
		return self.box_name
