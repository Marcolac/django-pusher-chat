from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^m/?$', 'chat.views.message', name='message'),
)
