from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from forms import UploadFileForm
from converter import *
from django.shortcuts import render_to_response, redirect
from django.core.context_processors  import csrf 
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.forms import forms
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.forms.util import ErrorList
import os

@csrf_exempt
def upload_file(request):
    file_types=""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and request.POST['1'] == 'xml':
            if '.xml' in request.FILES['file'].name:
                 form = UploadFileForm()
                 file_types = "input and output files have same type, please chose different type:"
            else:
                link = uploaded_file_toxml(request.FILES['file'])
                return HttpResponseRedirect('/'+link+'.xml/')
        if form.is_valid() and request.POST['1'] == 'json':
            if '.json' in request.FILES['file'].name:
                form = UploadFileForm()
                file_types = "input and output files have same type, please chose different type:"
            else:
                link = uploaded_file_tojson(request.FILES['file'])
                return HttpResponseRedirect('/'+link+'.json/')
        if form.is_valid() and request.POST['1'] == 'csv':
            if '.csv' in request.FILES['file'].name:
                form = UploadFileForm()
                file_types = "input and output files have same type, please chose different type:"
            else:
                link = uploaded_file_tocsv(request.FILES['file'])
                return HttpResponseRedirect('/'+link+'.csv/')
    else:
        form = UploadFileForm()
    return render_to_response('converter.html', {'form': form , 'type': file_types})
    
@csrf_exempt
def downloadfile(request,filepath): 
    path_to_file = "files/file_"+filepath.split('.')[0]
    fp=open(path_to_file,'rb')
    response = HttpResponse(fp)
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filepath)
    response['X-Sendfile'] = smart_str(path_to_file)
    return response   
