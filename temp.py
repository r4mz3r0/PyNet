from urllib.request import urlopen 
response = urlopen('http://www.packpub.com')
#response
print(response.readline())
