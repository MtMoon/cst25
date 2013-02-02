from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from account.settings import *

_SEX_RADIO=((True, 'Male'),
            (False, 'Female'))

class ModifForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=WIDGET_ATTR))
    password = forms.CharField(max_length=30, required=False,
                               widget=forms.PasswordInput(attrs=WIDGET_ATTR))
    confirmed_password = forms.CharField(max_length=30, required=False,
                                         widget=forms.PasswordInput(attrs=WIDGET_ATTR)) 
    birth = forms.DateField(widget=forms.DateInput(attrs=WIDGET_ATTR))
    sex = forms.BooleanField(required=False,
                             widget=forms.RadioSelect(choices=_SEX_RADIO, attrs=WIDGET_ATTR)) 
    signature = forms.CharField(max_length=200,
                               widget=forms.Textarea(attrs=WIDGET_ATTR))
    def clean(self):
        cleaned_data = super(ModifForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirmed = cleaned_data.get('confirmed_password')

        # Validate username
        if username:
            try:
                userobj = User.objects.get(username=username)
            except User.DoesNotExist:
                msg='User does not exist.'
                self._errors['username']=self.error_class([msg])
                del cleaned_data['username']

        # Validate password and confirmed password
        if password and confirmed:
            if password != confirmed:
                msg="Password and confirmed password didn't matches."
                self._errors['confirmed_password'] = self.error_class([msg])
                del cleaned_data['password']
                del cleaned_data['confirmed_password']
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=WIDGET_ATTR))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs=WIDGET_ATTR))
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                userobj = User.objects.get(username=username)
            except User.DoesNotExist:
                msg="User {0} does not exist".format(username)
                self._errors['username'] = self.error_class([msg])
                del cleaned_data['username']
                del cleaned_data['password']
                return cleaned_data
            userobj = authenticate(username=username, password=password)
            if userobj is None:
                msg="Username and password didn't match."
                self._errors['password'] = self.error_class([msg])
                del cleaned_data['password']
        return cleaned_data
