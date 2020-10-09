from lxml.html import fromstring 
import requests 
domain = input("Enter the domain ") 
url = 'http://whois.domaintools.com/' + domain 
headers = {'User-Agent': 'wswp'} 
resp = request.get(url, headers=headers) 
html = resp.text 

