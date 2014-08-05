# -*- coding: utf8 -*-
from django import forms

class UrlForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs= {'class':'form-control', 'required': 'true','placeholder': u'URL'}))

