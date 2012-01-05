from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from piston.resource import Resource

from senders.handlers import SenderGroupHandler
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/(?P<hash>[a-z0-9\-]+)/$', Resource(SenderGroupHandler)),
    url(r'^admin/', include(admin.site.urls)),
)
