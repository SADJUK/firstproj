# -*- coding: utf-8 -*-
from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.shortcuts import render_to_response




class UploadFileForm(forms.Form):
    file = forms.FileField(label = "выберите файл")
    def clean(self):
    	if len(self.cleaned_data)!=0:
    		if ('.xml' not in (self.cleaned_data['file'].name)) and ('.json' not in (self.cleaned_data['file'].name)) and ('.csv' not in (self.cleaned_data['file'].name)):
        		raise forms.ValidationError('input file type no validate')       		
    	return self.cleaned_data



	

 	