from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'emailCollection.views.displayHomepage', name='home'),
    url(r'^thankYou/$', 'emailCollection.views.displayThankYou', name='thankYou'),
)
