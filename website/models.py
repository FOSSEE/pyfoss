from django.db import models


class Nav(models.Model):
    """Main navigation links"""
    nav_name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    position = models.IntegerField()
    visible = models.BooleanField()

    def __str__(self):
        return self.nav_name


class SubNav(models.Model):
    """Navigation links for pages"""
    nav = models.ForeignKey(Nav, on_delete=models.CASCADE)
    subnav_name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    position = models.IntegerField()
    visible = models.BooleanField()

    def __str__(self):
        return self.subnav_name


class Page(models.Model):
    """Page that will be dispatched"""
    permalink = models.CharField(max_length=200, unique=True)
    heading = models.CharField(max_length=500)
    content = models.TextField()
    visible = models.BooleanField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.heading


class Block(models.Model):
    block_name = models.CharField(max_length=200)
    visible = models.BooleanField()

    def __str__(self):
        return self.block_name


class LinkBox(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    linkbox_name = models.CharField(max_length=200)
    position = models.IntegerField()
    visible = models.BooleanField()

    def __str__(self):
        return self.linkbox_name


class Link(models.Model):
    linkbox = models.ForeignKey(LinkBox, on_delete=models.CASCADE)
    link_name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    position = models.IntegerField()
    visible = models.BooleanField()

    def __str__(self):
        return self.link_name


class Banner(models.Model):
    title = models.CharField(max_length=500)
    banner = models.TextField(max_length=1000)
    position = models.IntegerField()
    visible = models.BooleanField()

    def __str__(self):
        return self.title


class TextBox(models.Model):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    textbox_name = models.CharField(max_length=200)
    content = models.TextField()
    position = models.IntegerField()
    visible = models.BooleanField()

    def __str__(self):
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
    no_of_participant = models.IntegerField()
    event_link = models.TextField()
    startdate = models.DateField()
    starttime = models.TimeField()
    enddate = models.DateField()
    endtime = models.TimeField()
    venue = models.CharField(max_length=500)
    street = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField(default=0)

    class Meta:
        db_table = 'workshop'
