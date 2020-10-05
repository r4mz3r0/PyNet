import urllib
import json
from urllib.request import urlopen 
#-------------2-----------
import urllib.request
""" - Multiline Comment (/**/ for C/Java)
With packages, like this, you sometimes need to explicitly import the piece you want. urllib module does not load everything. 
"""
url = "http://www.google.com"
#-------------------------
response = urlopen(url)
#response -- Does not work for packtpub, use google.com
print(response.readline())


#-----------2--------------
print(urllib.request.urlopen(url, timeout=30))

#--------------------------

#3 if the response is in JSON format
response = urllib.request.urlopen(url, timeout=30)
json_response = json.loads(response.read())

