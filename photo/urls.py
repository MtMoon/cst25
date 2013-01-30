from django.conf.urls import patterns, include, url

urlpatterns = patterns('photo.views',
                       url(r'^$', 'show_homepage_first'),
                       url(r'^(?P<nr>\d+)/$', 'show_homepage'), 
                       url(r'^album/(?P<album_id>\d+)/$',
                           'show_album_first'), 
                       url(r'^album/(?P<album_id>\d+)/(?P<nr>\d+)/$',
                           'show_album'),
                       url(r'^photo/(?P<photo_id>\d+)/$',
                           'show_photo'), 
                       )

def wrap_photo_url(num):
    return "/photo/photo/{0}/".format(num)

def wrap_album_url(num, page):
    return "/photo/album/{0}/{1}/".format(num, page)

def str_album_page(alid):
    return "/photo/album/{0}/".format(alid)+"{0}/"

def str_homepage():
    return "/photo/{0}/"
