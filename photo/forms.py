from django import forms

ATTRS={'class': 'widget'}

class CommentForm(forms.Form):
    comment=forms.CharField(max_length=200,
                            widget=forms.Textarea(attrs=ATTRS))

