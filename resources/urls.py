from django.conf.urls import patterns, include, url

urlpatterns = patterns('resources.views',
                       url(r'^$', 'show_homepage_first'),
                       url(r'^(?P<nr>\d+)/$', 'show_homepage'), 
                       url(r'^catalog/(?P<catalog_id>\d+)/$',
                           'show_catalog_first'), 
                       url(r'^catalog/(?P<catalog_id>\d+)/(?P<nr>\d+)/$',
                           'show_catalog'),
                       )

def wrap_catalog_url(catid):
    return "/resources/catalog/{0}/".format(catid)

def str_homepage_url():
    return "/resources/{0}/"

def str_catalog_url(catid):
    return "/resources/catalog/{0}/".format(catid) + "{0}/"
