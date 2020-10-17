import requests 
response = requests.get('https://www.debian.org/releases/stable/index.en.html') 
from lxml.etree import HTML 
root = HTML(response.content) 
