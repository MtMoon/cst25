from django import forms
from account.settings import *

_SEX_RADIO=(('1', 'Male'),
            ('0', 'Female'))

class ModifForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=WIDGET_ATTR))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs=WIDGET_ATTR)) 
    confirm_password = forms.CharField(max_length=30,
                                       widget=forms.PasswordInput(attrs=WIDGET_ATTR)) 
    birth = forms.DateField(widget=forms.DateInput(attrs=WIDGET_ATTR))
    sex = forms.CharField(max_length=1,
                         widget=forms.RadioSelect(choices=_SEX_RADIO, attrs=WIDGET_ATTR)) 
    signature = forms.CharField(max_length=200,
                               widget=forms.Textarea(attrs=WIDGET_ATTR)) 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=WIDGET_ATTR))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs=WIDGET_ATTR))
    next = forms.CharField(max_length=30,
                           widget=forms.HiddenInput(attrs=WIDGET_ATTR),
                           initial=LOGIN_REDIRECT_URL)

