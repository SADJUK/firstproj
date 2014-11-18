import json
import urllib
import dicttoxml

def json2xml(file):
	obj = json.loads(file)
	print(obj)
	xml = dicttoxml.dicttoxml(obj)
	print(xml)