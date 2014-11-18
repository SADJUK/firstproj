from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^(?P<filepath>(.*))/', 'converter.views.downloadfile'),
    url(r'^', 'converter.views.upload_file'), 
)    
