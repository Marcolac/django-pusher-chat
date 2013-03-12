from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^ms/?$', 'chat.views.message', name='message'),
)
