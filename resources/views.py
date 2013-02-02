from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from resources.models import Catalog, ResFile
from resources.urls import wrap_catalog_url, str_homepage_url, str_catalog_url
from resources.settings import *
from libs.page import get_page_dict, apage

@login_required
def show_homepage_first(request):
    return show_homepage(request, 1)

@login_required
def show_catalog_first(request, catalog_id):
    return show_catalog(request, catalog_id, 1)

@login_required
def show_homepage(request, nr):
    catalog_list = apage(Catalog.objects.all(), int(nr), CATALOG_NPP)
    # No album actually in this page.
    if not catalog_list and nr != 1:
        return HttpResponseRedirect('/resources/1/')
    return render_to_response('res_all.html',
                              {'catalog_list': catalog_list,
                               'page':get_page_dict(Catalog.objects.all(),
                                                    CATALOG_NPP, str_homepage_url(), int(nr))},
                              context_instance=RequestContext(request))
@login_required
def show_catalog(request, catalog_id, nr):
    try:
        catalog = Catalog.objects.get(pk=catalog_id)
    except Catalog.DoesNotExist:
        return HttpResponseRedirect('/resources/')
    res_list = apage(ResFile.objects.filter(catalog__id=catalog_id), int(nr), RES_NPP)
    if not res_list and nr != 1:
        return HttpResponseRedirect(wrap_catalog_url(catalog_id, 1))
    return render_to_response('res_cat.html',
                              {'res_list':res_list,
                               'catalog':catalog,
                               'page':get_page_dict(ResFile.objects.filter(catalog__id=catalog_id),
                                                    RES_NPP,
                                                    str_catalog_url(catalog_id),
                                                    int(nr))},
                              context_instance=RequestContext(request))
