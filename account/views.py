from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from account.forms import ModifForm, LoginForm
from account.procedures import check_modify, get_profile, form_load, NoSuchUser
from account.settings import *

@login_required
def modify(request):
    if request.method == 'GET':
        try:
            form = form_load(request.user.username)
        except NoSuchUser:
            return HttpResponseRedirect('/account/')
        return render_to_response('acc_mdf.html',
                                  { 'form': form },
                                  context_instance=RequestContext(request))
    else: # request.method == 'POST'
        form = ModifForm(request.POST)
        try:
            success = check_modify(request, form)
        except NoSuchUser:
            return HttpResponseRedirect('/account/')
        if success:
            return HttpResponseRedirect('/account/')
        else:
            return render_to_response('acc_mdf.html',
                                      { 'form': form },
                                      context_instance=RequestContext(request))
        
@login_required
def details(request, username):
    try:
        userobj = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404
    profile = get_profile(userobj)
    return render_to_response('acc_detail.html',
                              { 'acc': profile },
                              context_instance=RequestContext(request))

@login_required
def details_myself(request):
    return details(request, request.user.username)

def view_login(request):
    if request.user.is_authenticated():
        try:
            return HttpResponseRedirect(request.REQUEST['next'])
        except KeyError:
            return HttpResponseRedirect(LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        return do_login(request)
    else:
        return render_to_response('acc_login.html',
                                  {'form': LoginForm() },
                                  context_instance=RequestContext(request))

def do_login(request):
    try:
        nexturl = request.REQUEST['next']
    except KeyError:
        nexturl = LOGIN_REDIRECT_URL
    form = LoginForm(request.POST)
    if not form.is_valid():
        return render_to_response('acc_login.html',
                                  {'form': form },
                                  context_instance=RequestContext(request))
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    user = authenticate(username=username, password=password)
    if not user or not user.is_active:
        form.errors['username'] = "No such User"
        return render_to_response('acc_login.html',
                                  {'form': form },
                                  context_instance=RequestContext(request))
    login(request, user)
    return HttpResponseRedirect(nexturl)

def do_logout(request):
    logout(request)
    try:
        return HttpResponseRedirect(request.REQUEST['next'])
    except KeyError:
        return HttpResponseRedirect(LOGOUT_REDIRECT_URL)
