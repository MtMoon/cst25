from django.contrib.auth.models import User
from account.models import UserProfile
from account.forms import ModifForm

class NoSuchUser(Exception):
    def __init__(self, value=''):
        self.value = value
    def __str__(self):
        return repr(self.value)

def check_modify(request, form):
    if not form.is_valid():
        return False
    try:
        userobj = User.objects.get(username=form.cleaned_data['username'])
    except User.DoesNotExist:
        raise NoSuchUser
    profile = get_profile(userobj)
    profile.birth = form.cleaned_data['birth']
    if form.cleaned_data['password']:
        userobj.set_password(form.cleaned_data['confirmed_password'])
        userobj.save()
    profile.sex = form.cleaned_data['sex']
    profile.signature = form.cleaned_data['signature']
    profile.save()
    return True

def form_load(uname):
    try:
        userobj = User.objects.get(username=uname)
    except User.DoesNotExist:
        raise NoSuchUser
    profile = get_profile(userobj)
    formdata = {'username': uname,
                'password': '',
                'birth': profile.birth,
                'sex': profile.sex,
                'signature': profile.signature }
    form = ModifForm(formdata)
    return form

def get_profile(userobj):
    try:
        profile = UserProfile.objects.get(user=userobj)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=userobj)
        profile.save()
    return profile
