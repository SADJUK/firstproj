from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import dicttoxml
import json
import csv
from xmlutils.xml2csv import xml2csv
from xmlutils.xml2json import xml2json
import os


dir_to_file="files/file"#os.path.join(PROJECT_DIR, 'files/file')


def uploaded_file_toxml(f):
	if f.name.split('.')[1] == 'json':
		str_obj=""
		for chunk in f.chunks():
			str_obj+=chunk
		try:
			obj = json.loads(str_obj)
 			xml = dicttoxml.dicttoxml(obj)
 		except:
 			xml="<catalog>input file not .json</catalog>" 
		path = default_storage.save(dir_to_file, ContentFile(xml))
		return path.split('file_')[1]

	if f.name.split('.')[1] == 'csv':
		path = default_storage.save(dir_to_file, f)
		return path.split('file_')[1]


def uploaded_file_tojson(f):
	if f.name.split('.')[1] == 'xml':
		try:
			converter = xml2json(f, encoding="utf-8")
			json=converter.get_json()
		except:
			json={"input":"input file type not .xml"}
		path = default_storage.save(dir_to_file, ContentFile(json))
		return path.split('file_')[1]

	if f.name.split('.')[1] == 'csv':
		path = default_storage.save(dir_to_file, f)
		return path.split('file_')[1]


def uploaded_file_tocsv(f):
	if f.name.split('.')[1] == 'json':
		path = default_storage.save(dir_to_file, f)
		return path.split('file_')[1]

	if f.name.split('.')[1] == 'xml':
		path = default_storage.save(dir_to_file, f)
		return path.split('file_')[1]
