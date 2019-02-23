from django.conf.urls import include, url, re_path
from .views import dispatcher
from . import views
app_name = 'website'
urlpatterns = [

    # Main pages dispatcher
    re_path(r'^$', dispatcher, name="home"),
    re_path(r'^(?P<permalink>.+)/$', dispatcher, name="dispatcher"),
]
