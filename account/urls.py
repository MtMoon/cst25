from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'account.views.view_login'),
    url(r'^logout/$', 'account.views.do_logout'),
    url(r'^modify/$', 'account.views.modify'),
    url(r'^details/(?P<username>.*)/$', 'account.views.details'),
    url(r'^$', 'account.views.details_myself'),
)
