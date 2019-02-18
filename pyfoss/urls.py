from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Examples:
    # url(r'^$', 'pyfoss.views.home', name='home'),
    # url(r'^pyfoss/', include('pyfoss.foo.urls')),
    url(r'^', include('website.urls', namespace='website')),
]
