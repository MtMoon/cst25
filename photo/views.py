from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from photo.models import Album, Photo, Comment
from photo.urls import wrap_photo_url, wrap_album_url, str_album_page
from photo.urls import str_homepage
from photo.settings import *
from libs.page import get_page_dict, apage

def show_homepage_first(request):
    return show_homepage(request, 1)

def show_album_first(request, album_id):
    return show_album(request, album_id, 1)

def show_homepage(request, nr):
    album_list = apage(Album.objects.all(), int(nr), ALBUM_NPP)
    # No album actually in this page.
    if not album_list and nr != 1:
        return HttpResponseRedirect('/photo/1/')
    return render_to_response('photo_homepage.html',
                              {'album_list':album_list,
                               'page':get_page_dict(Album.objects.all(),
                                                    ALBUM_NPP, str_homepage(), int(nr))},
                              context_instance=RequestContext(request))

def show_album(request, album_id, nr):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        return HttpResponseRedirect('/photo/')
    photo_list = apage(Photo.objects.filter(album__id=album_id), int(nr), PHOTO_NPP)
    if not photo_list and nr != 1:
        return HttpResponseRedirect(wrap_album_url(album_id, 1))
    return render_to_response('photo_album.html',
                              {'photo_list':photo_list,
                               'album':album,
                               'page':get_page_dict(Photo.objects.filter(album__id=album_id),
                                                    PHOTO_NPP,
                                                    str_album_page(album_id),
                                                    int(nr))},
                              context_instance=RequestContext(request))
    

def show_photo(request, photo_id):
    photo_resp = {}
    try:
        photo = Photo.objects.get(pk=photo_id)
    except Photo.DoesNotExist:
        return HttpResponseRedirect('/photo/')
    photo_resp['url'] = photo.url()
    photo_resp['img'] = photo.img()
    photo_resp['desc'] = photo.desc
    # Get the ids of previous and next photos.
    photo_list = Photo.objects.filter(album__pk=photo.album.id)
    if photo_list.count() == 1:
        photo_resp['prev'] = -1
        photo_resp['next'] = -1
    elif photo_list[0].id == int(photo_id):
        photo_resp['prev'] = -1
        photo_resp['next'] = wrap_photo_url(photo_list[1].id)
    elif photo_list[photo_list.count()-1].id == int(photo_id):
        photo_resp['prev'] = wrap_photo_url(photo_list[photo_list.count()-2].id)
        photo_resp['next'] = -1
    else:
        for i in range(photo_list.count()):
            if photo_list[i].id == int(photo_id):
                photo_resp['prev'] == wrap_photo_url(photo_list[i-1].id)
                photo_resp['next'] == wrap_photo_url(photo_list[i+1].id)
                break
    comment = Comment.objects.filter(photo__pk=photo_id)
    return render_to_response('photo_view.html',
                              {'photo': photo_resp,
                               'album': photo.album,
                               'comment_list': comment},
                              context_instance=RequestContext(request));

