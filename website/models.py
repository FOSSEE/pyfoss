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
		return self.textbox_name
"""
Models from fossee_new Database created using inspectdb
Use it with the "fossee_in" database eg:using("fossee_in")
These models are used only for django orm reference.
"""
CATEGORY = (("fluid mechanics", "Fluid Mechanics"),
            ("control systems", "Control Theory & Control Systems"),
            ("chemical engineering", "Chemical Engineering"),
            ("thermodynamics", "Thermodynamics"),
            ("mechanical engineering", "Mechanical Engineering"),
            ("signal processing", "Signal Processing"),
            ("digital communications", "Digital Communications"),
            ("electrical technology", "Electrical Technology"),
            ("maths & science", "Mathematics & Pure Science"),
            ("analog electronics", "Analog Electronics"),
            ("digital electronics", "Digital Electronics"),
            ("computer programming", "Computer Programming"),
            ("others", "Others"))

class FOSSEEStats(models.Model):
	w_id = models.IntegerField(unique=True, primary_key=True)
	foss_name = models.CharField(max_length=500)
	type = models.CharField(max_length=50)
	w_name = models.CharField(max_length=500)
	body = models.TextField()
	no_of_participant	 = models.IntegerField(max_length=5)
	event_link = models.TextField()
	startdate = models.DateTimeField()
	starttime = models.TimeField()
	enddate = models.DateTimeField()
	endtime = models.TimeField()
	venue = models.CharField(max_length=500)
	street = models.CharField(max_length=500)
	country = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	pincode = models.IntegerField(default=0)
	class Meta:
		db_table = 'workshop'

class TBCPYTHONBook(models.Model):
	title = models.CharField(max_length=500)
	author = models.CharField(max_length=300)
	category = models.CharField(max_length=32, choices=CATEGORY)
	publisher_place = models.CharField(max_length=150)
	isbn = models.CharField(max_length=50)
	edition = models.CharField(max_length=15)
	year_of_pub = models.CharField(max_length=4)
	no_chapters = models.IntegerField(default=0, blank=True)
	contributor = models.IntegerField(default=0, blank=True)
	reviewer = models.IntegerField(default=0, blank=True)
	approved = models.BooleanField(default=False)
	start_time = models.DateField(null=True, default=None)
	end_time = models.DateField(null=True, default=None)
	class Meta:
		db_table = 'tbc_book'

