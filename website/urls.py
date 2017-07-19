from django.conf.urls import  include, url
from .views import dispatcher
urlpatterns = [

	# Main pages dispatcher
	url(r'^$', dispatcher, name="home"),
	url(r'^(?P<permalink>.+)/$', dispatcher, name="dispatcher"),
]
