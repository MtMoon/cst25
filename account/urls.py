from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'account.views.login'),
    url(r'^logout/$', 'account.views.do_logout'),
    url(r'^modify/$', 'account.views.modify'),
    url(r'^details/(?<username>.*)/$', 'account.views.details'),
    url(r'^$', 'account.views.details_myself'),
)
