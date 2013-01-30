from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cst25 import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^photo/', include('photo.urls')),
    # Examples:
    # url(r'^$', 'cst25.views.home', name='home'),
    # url(r'^cst25/', include('cst25.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()
