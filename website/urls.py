from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	# Main pages dispatcher
	url(r'^$', 'website.views.dispatcher', name="home"),
	url(r'^(?P<permalink>.+)/$', 'website.views.dispatcher', name="dispatcher"),
)
